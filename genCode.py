#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, \
    unicode_literals

from io import open

import json
import os
import re
import six
import sys
import textwrap

from jinja2 import Environment, FileSystemLoader

from taskcluster.runtimeclient import ROUTING_KEY_BLACKLIST

BASE_DIR = os.path.dirname(__file__)
GENERATED_STRING = "# This file is generated!  Do not edit!"
CODE_DEFS = {
    "sync": {
        "clientModule": "taskcluster.sync.syncclient",
        "clientClass": "SyncClient",
        "codeDir": os.path.join(BASE_DIR, 'taskcluster', "sync"),
        "testDir": os.path.join(BASE_DIR, 'test'),
        "testTemplate": "test.template",
        "defStatement": "def",
        "returnStatement": "return",
    },
    "async": {
        "clientModule": "taskcluster.async.asyncclient",
        "clientClass": "AsyncClient",
        "codeDir": os.path.join(BASE_DIR, 'taskcluster', "async"),
        "testDir": os.path.join(BASE_DIR, 'test', "async"),
        "testTemplate": "async_test.template",
        "returnStatement": "return await",
        "defStatement": "async def",
    },
}


def loadJson(filename):
    with open(filename) as fh:
        return json.load(fh)


def createInitPy(pydir, name, modules):
    initpy = os.path.join(pydir, '__init__.py')
    print(initpy)
    with open(initpy, 'w') as fh:
        print("#!/usr/bin/env python", file=fh)
        print(GENERATED_STRING, file=fh)
        for module in modules:
            print("from taskcluster.{name}.{module} import {module}".format(
                  name=name, module=module), file=fh)
        print("__all__ = [", file=fh)
        for module in modules:
            print("    {module},".format(module=module), file=fh)
        print("]", file=fh)


def createRoutes(api):
    """Create a string to define self.routes.
    """
    routes = ''
    for entry in api['entries']:
        if entry['type'] == 'function':
            routes += "'%s': '%s',\n" % (entry['name'], anglesToBraces(entry['route']))
    return routes


def createRoutingKeys(api):
    """Create a string to define self.routingKey

    This doesn't include everything in routingKey, because
        a) only a few things are currently used, and
        b) for the sake of line and file length
    """
    parts = []
    for entry in api['entries']:
        if 'routingKey' in entry:
            parts.append("    '%s': [" % entry['name'])
            for routingKey in entry['routingKey']:
                parts.append("        {")
                for key in sorted(routingKey.keys()):
                    if key not in ROUTING_KEY_BLACKLIST:
                        value = routingKey[key]
                        if isinstance(value, (six.binary_type, six.text_type)):
                            value = "'{}'".format(value)
                        parts.append("            '%s': %s," % (key, value))
                parts.append("        },")
            parts.append("    ],")
    return '\n'.join(parts)


def argumentString(entry, methodArgs=False):
    """Returns a comma-delimited argument string for the given function.

    When methodArgs is True, add 'self' and other args/kwargs for a method
    definition (for code.template).

    When it's False, just return the arguments + payload as defined in the
    api, but single quoted (for test.template).
    """
    parts = []
    if methodArgs:
        parts.append('self')
    if 'args' in entry:
        parts.extend(entry['args'])
    if 'input' in entry:
        inputName = 'payload'
        parts.append(inputName)
    if methodArgs:
        if entry.get('query'):
            parts.append('options=None')
        return ", ".join(parts)
    else:
        string = ""
        for p in parts:
            string += "'{}', ".format(p)
        return string


def anglesToBraces(s):
    '''
    Returns a string with <vars> replaced by {vars}
    '''
    if s:
        return re.sub('<(.*?)>', '{\\1}', s)


def render(env, templateName, serviceName, apiDefn, codeDefn):
    template = env.get_template(templateName)
    api = apiDefn['reference']
    url = apiDefn['referenceUrl']
    return template.render(
        serviceName=serviceName,
        api=api,
        argumentString=argumentString,
        createRoutes=createRoutes,
        createRoutingKeys=createRoutingKeys,
        generatedString=GENERATED_STRING,
        referenceUrl=url,
        **codeDefn
    )


def typesetDocstring(s, level=4):
    lines = []
    wrapper = textwrap.TextWrapper(subsequent_indent=' ' * level,
                                   expand_tabs=True, width=100)
    for line in s.splitlines():
        if line == '':
            lines.append('')
        lines.extend(wrapper.wrap(line))
        wrapper.initial_indent = ' ' * level

    return '\n'.join(lines)


def renderCode(name, apiDefn, codeDefn):
    env = Environment(loader=FileSystemLoader('templates'))
    env.filters['docstring'] = typesetDocstring
    env.filters['anglesToBraces'] = anglesToBraces
    code = render(env, 'code.template', name, apiDefn, codeDefn)
    with open(os.path.join(codeDefn['codeDir'], '{}.py'.format(name)),
              'w', encoding='utf-8') as fh:
        print(code, file=fh)
    test = render(env, codeDefn['testTemplate'], name, apiDefn, codeDefn)
    with open(os.path.join(codeDefn['testDir'], 'test{}.py'.format(name)),
              'w', encoding='utf-8') as fh:
        print(test, file=fh)


if __name__ == '__main__':
    jsonFile = os.environ.get(
        "APIS_JSON",
        os.path.join(BASE_DIR, "taskcluster", "apis.json")
    )
    apiDef = loadJson(jsonFile)
    for key, value in CODE_DEFS.items():
        codeDir = value['codeDir']
        if not os.path.exists(codeDir):
            os.makedirs(codeDir)
        createInitPy(codeDir, key, sorted(apiDef.keys()))
        for name, defn in apiDef.items():
            print("{} {}".format(key, name))
            renderCode(name, defn, value)
