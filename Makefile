.PHONY:	help	lint-python	format-python

help:
	@echo "lint-python       -    Python Lint by Flake8."
	@echo "format-python     -    Python code format by Black."

lint-python:
	flake8 .

format-python:
	black .
