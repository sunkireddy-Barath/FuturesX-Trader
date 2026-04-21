.PHONY: setup test run shell clean help

help:
	@echo "Available commands:"
	@echo "  make setup   - Create venv and install dependencies"
	@echo "  make test    - Run unit tests"
	@echo "  make run     - Run the bot in interactive mode"
	@echo "  make clean   - Remove venv and temporary files"

setup:
	bash setup.sh

test:
	PYTHONPATH=. ./venv/bin/python3 tests/test_validators.py

run:
	./venv/bin/python3 cli.py --interactive

ui:
	PYTHONPATH=. ./venv/bin/python3 web/app.py

clean:
	rm -rf venv
	rm -rf trading_bot.log
	find . -type d -name "__pycache__" -exec rm -rf {} +
