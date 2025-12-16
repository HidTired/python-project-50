install:
    uv sync

lint:
    uv run ruff check .

test:
    uv run pytest tests/

test-coverage:
    uv run pytest --cov=gendiff --cov-report=html --cov-report=term-missing