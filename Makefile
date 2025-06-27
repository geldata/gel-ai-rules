render:
	python3 main.py

format:
	ruff format .

lint:
	ruff check .

typecheck:
	mypy .

check: format lint typecheck

check-render:
	make render
	git diff --exit-code

.PHONY: render format lint typecheck check check-render