 ### Defensive settings for make:
#     https://tech.davis-hansson.com/p/make/
SHELL:=bash
.ONESHELL:
.SHELLFLAGS:=-xeu -o pipefail -O inherit_errexit -c
.SILENT:
.DELETE_ON_ERROR:
MAKEFLAGS+=--warn-undefined-variables
MAKEFLAGS+=--no-builtin-rules

# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`


# Specifcs of this Makefile
PIP_VERSION=21.3
PIP_PARAMS=--src devsrc --use-deprecated legacy-resolver

# install and run
.PHONY: all
all: install run

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: .installed.txt ## pip install all dependencies and scripts

.installed.txt: requirements_barebone.txt constraints.txt sources.ini
	@pip install -U "pip==${PIP_VERSION}" wheel mxdev
	@mxdev -c sources.ini
	@pip install -r requirements-dev.txt ${PIP_PARAMS}
	@pip freeze >.installed.txt


test: install
	@zope-testrunner --test-path=src

run: install  ## run Plone
	@pserve dev.ini

.PHONY: clean
clean: install  ## remove instance configuration (keep data)
	@pip uninstall -y -r requirements-dev.txt
	@rm .installed.txt

.PHONY: style
style: install  ## format code (black, isort, zpretty)
	@isort src
	@black src
	@find src -name "*.zcml"|xargs zpretty -iz
	@find src -name "*.xml"|grep -v locales|xargs zpretty -ix
