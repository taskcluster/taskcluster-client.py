#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, \
    unicode_literals

from io import open

import json
import os
import re
import six
import textwrap

from jinja2 import Environment, FileSystemLoader

GENERATED_STRING = "# This file is generated!  Do not edit!"
# ROUTING_KEY_WHITELIST is also defined in test/base/__init__.py
# if you change it, please update it there as well.
ROUTING_KEY_WHITELIST = ("name", "multipleWords", "constant")


def loadJson(filename):
    with open(filename) as fh:
        return json.load(fh)


def createInitPy(pydir, modules):
    initpy = os.path.join(pydir, '__init__.py')
    print(initpy)
    with open(initpy, 'w') as fh:
        print("#!/usr/bin/env python", file=fh)
        print(GENERATED_STRING, file=fh)
        for module in modules:
            print("from taskcluster.sync.{module} import {module}".format(module=module),
                  file=fh)
        print("__all__ = [", file=fh)
        for module in modules:
            print("    {module},".format(module=module), file=fh)
        print("]", file=fh)


def createUrls(api):
    """Create a string to define self.urls.
    """
    urls = ''
    for entry in api['entries']:
        if entry['type'] == 'function':
            urls += "'%s': '{baseUrl}%s',\n" % (entry['name'], anglesToBraces(entry['route']))
    return urls


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
                for key in ROUTING_KEY_WHITELIST:
                    if key in routingKey:
                        value = routingKey[key]
                        if isinstance(value, (six.binary_type, six.text_type)):
                            value = "'{}'".format(value)
                        parts.append("            '%s': %s," % (key, value))
                parts.append("        },")
            parts.append("    ],")
    return '\n'.join(parts)


def methodArgumentString(entry):
    """Returns an argument string for the given function
    """
    parts = ['self']
    parts.extend(argumentNames(entry))
    if entry['method'] == 'get':
        parts.append('signUrl=False')
    return ", ".join(parts)


def argumentNames(entry):
    parts = []
    if 'args' in entry:
        parts.extend(entry['args'])
    if 'input' in entry:
        inputName = 'payload'
        parts.append(inputName)
    return parts


def argumentString(entry):
    """Returns a string of a list of argument names, sans self and signUrl
    """
    string = ''
    for name in argumentNames(entry):
        string += "'{name}', ".format(name=name)
    return string


def anglesToBraces(s):
    '''
    Returns a string with <vars> replaced by {vars}
    '''
    if s:
        return re.sub('<(.*?)>', '{\\1}', s)


def render(env, templateName, serviceName, defn):
    template = env.get_template(templateName)
    api = defn['reference']
    url = defn['referenceUrl']
    return template.render(
        serviceName=serviceName,
        api=api,
        methodArgumentString=methodArgumentString,
        argumentString=argumentString,
        createUrls=createUrls,
        createRoutingKeys=createRoutingKeys,
        generatedString=GENERATED_STRING,
        referenceUrl=url,
    )


def docstringify(s, level=4):
    lines = []
    wrapper = textwrap.TextWrapper(subsequent_indent=' ' * level,
                                   expand_tabs=True, width=100)
    for line in s.splitlines():
        if line == '':
            lines.append('')
        lines.extend(wrapper.wrap(line))
        wrapper.initial_indent = ' ' * level

    return '\n'.join(lines)


def renderCode(name, defn, codeDir, testDir):
    env = Environment(loader=FileSystemLoader('templates'))
    env.filters['docstring'] = docstringify
    env.filters['anglesToBraces'] = anglesToBraces
    code = render(env, 'code.template', name, defn)
    with open(os.path.join(codeDir, '{}.py'.format(name)),
              'w', encoding='utf-8') as fh:
        print(code, file=fh)
    test = render(env, 'test.template', name, defn)
    with open(os.path.join(testDir, 'test{}.py'.format(name)),
              'w', encoding='utf-8') as fh:
        print(test, file=fh)


if __name__ == '__main__':
    baseDir = os.path.dirname(__file__)
    jsonFile = os.environ.get(
        "APIS_JSON",
        os.path.join(baseDir, "taskcluster", "apis.json")
    )
    codeDir = os.path.join(baseDir, 'taskcluster', 'sync')
    testDir = os.path.join(baseDir, 'test')
    if not os.path.exists(codeDir):
        os.makedirs(codeDir)
    apiDef = loadJson(jsonFile)
    createInitPy(codeDir, sorted(apiDef.keys()))
    for name, defn in apiDef.items():
        print(name)
        renderCode(name, defn, codeDir, testDir)
