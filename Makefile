# Python makefile

.PHONY: install learn estimate clean help
.DEFAULT: help

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check code with pylint"
	@echo "format - format code with yapf"
	@echo "test - run tests quickly with the default Python"
	@echo "install - install python and the dependencies"
	@echo "learn - run the learning process"
	@echo "estimate - estimate the cost"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	pylint src/

format:
	yapf -i -r src

test:
	@echo "No tests for the moment..."

install:
	sudo apt-get -y install python3 python3-pip
	pip3 install -r requirements.txt

learn:
	@echo "Learning..."
	${PYTHON} src/train.py

estimate:
	@echo "Estimating..."
	${PYTHON} src/estimate.py

