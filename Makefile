.PHONY: install test run clean

install:
	python -m pip install -r requirements.txt

test:
	pytest

run:
	python main.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
