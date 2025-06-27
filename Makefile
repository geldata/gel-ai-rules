render:
	python3 main.py

format:
	ruff format .

lint:
	ruff check .

typecheck:
	mypy .

check: format lint typecheck

.PHONY: render format lint typecheck check