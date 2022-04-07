SHELL := /bin/env zsh

all: install run

install:
	@echo "installing the project dependencies..."
	pip install -r requirements.txt

run:
	@echo "running the project..."
	python -m src