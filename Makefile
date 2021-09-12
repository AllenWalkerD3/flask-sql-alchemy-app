source_dir := $(CURDIR)/src
tests_dir := $(CURDIR)/tests_dir
build_dir := $(CURDIR)/build
dist_dir := $(CURDIR)/dist

PYTHONPATH += $(source_dir)
ENV_NAME ?= env
PIPENV_PACKAGE ?=
make_env = python3 -m venv $(ENV_NAME)
# make_env = pipenv install $(PIPENV_PACKAGE)
env_dir = $(CURDIR)/$(ENV_NAME)
bin_dir = $(env_dir)/bin
activate_env = . $(bin_dir)/activate
dotenv_file = .env

STAGE ?= dev
CONFIG_VARIABLE_NAME = PAYCHECK_SETTINGS
CONFIG_FILENAME = $(CURDIR)/$(STAGE)-settings.cfg

define create-venv
	@echo Creating $@...
	$(make_env)
	$(bin_dir)/pip install --upgrade pip
	$(bin_dir)/pip install pip-tools
endef

env:
	$(create-venv)

.PHONY: install
install: env
	$(bin_dir)/pip-sync requirements.txt dev-requirements.txt

.PHONY: run
run:
	PYTHONPATH=$(PYTHONPATH) 					\
	$(CONFIG_VARIABLE_NAME)=$(CONFIG_FILENAME)	\
	$(bin_dir)/python app.py

.PHONY: serve
serve:
	PYTHONPATH=$(PYTHONPATH) 					\
	$(CONFIG_VARIABLE_NAME)=$(CONFIG_FILENAME)	\
	${activate_env} && sls wsgi serve

.PHONY: create_table
create_table:
	PYTHONPATH=$(PYTHONPATH) 					\
	$(CONFIG_VARIABLE_NAME)=$(CONFIG_FILENAME)	\
	$(bin_dir)/python src/create_table.py