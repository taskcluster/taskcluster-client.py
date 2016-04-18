PYTHON := python
TOX_ENV ?= py35
VENV := .tox/$(TOX_ENV)
PY2VENV := .tox/py27
PY3VENV := .tox/py35

JS_CLIENT_BRANCH=master
APIS_JSON=$(PWD)/taskcluster/apis.json
APIS_JS_HREF=https://raw.githubusercontent.com/taskcluster/taskcluster-client/$(JS_CLIENT_BRANCH)/lib/apis.js

.PHONY: test
test: nosetests lint

.PHONY: nosetests
nosetests: $(VENV)/bin/python
	$(VENV)/bin/python setup.py test $$TEST_ARGS
	$(VENV)/bin/coverage html

.PHONY: lint
lint: $(VENV)/bin/python $(PY2VENV)/bin/python
	$(PY3VENV)/bin/flake8 --max-line-length=100 taskcluster test
	$(PY2VENV)/bin/flake8 --max-line-length=100 --exclude="async,asyncutils.py" taskcluster test

.PHONY: update
update: update-api gencode update-readme docs

.PHONY: update-api
update-api: $(VENV)/bin/python
	API_REF_OUT="$(APIS_JSON)" $(VENV)/bin/python fetchApi.py
	@python -mjson.tool $(APIS_JSON) > /dev/null || echo "apis.json cannot be parsed by python's JSON"

.PHONY: gencode
gencode: $(VENV)/bin/python
	APIS_JSON="$(APIS_JSON)" $(VENV)/bin/python genCode.py

.PHONY: update-readme
update-readme: $(VENV)/bin/python
	README_FILE=README.md APIS_JSON=$(APIS_JSON) $(VENV)/bin/python genDocs.py

$(PY3VENV)/bin/python:
	tox --notest -e py35
	$(PY3VENV)/bin/pip install --upgrade setuptools
	$(PY3VENV)/bin/python devDep.py
	$(PY3VENV)/bin/python setup.py develop

$(PY2VENV)/bin/python:
	tox --notest -e py27
	$(PY2VENV)/bin/pip install --upgrade setuptools
	$(PY2VENV)/bin/python devDep.py
	$(PY2VENV)/bin/python setup.py develop

.PHONY: dev-env
dev-env: $(VENV)/bin/python

.PHONY: clean
clean:
	rm -rf node-$(NODE_VER)-$(NODE_PLAT) node_modules
	rm -rf *.egg *.egg-info dist/
	find . -name "*.py?" -exec rm {} +
	rm -rf .tox htmlcov .coverage nosetests.xml
	rm -rf env-*

.PHONY: docs
docs:
	rm -rf docs/_build
	$(VENV)/bin/python -mpip install sphinx
	$(VENV)/bin/python makeRst.py > docs/client.rst
	LC_CTYPE= make -C docs html SPHINXBUILD=$(abspath $(VENV)/bin/sphinx-build)

run_python: $(VENV)/bin/python
	$(VENV)/bin/python testscript.py
