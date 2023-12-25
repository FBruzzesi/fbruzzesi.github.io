init-env:
	python -m pip install -r requirements/core.txt --no-cache-dir

init-dev:
	python -m pip install -r requirements/core.txt -r requirements/dev.txt -r requirements/blog.txt --no-cache-dir

typo:
	typos automation docs

lint:
	ruff version
	ruff check automation --fix
	ruff format automation
	ruff clean

serve:
	mkdocs serve

deploy:
	mkdocs gh-deploy

clean:
	rm -rf __pycache__ */__pycache__ */**/__pycache__ \
		.pytest_cache */.pytest_cache */**/.pytest_cache \
		.ruff_cache */.ruff_cache */**/.ruff_cache \
		.mypy_cache */.mypy_cache */**/.mypy_cache \
		site build dist htmlcov .coverage .tox

check: typo lint clean
