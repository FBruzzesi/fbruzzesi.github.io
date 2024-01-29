init-env:
	python -m pip install -r requirements/core.txt --no-cache-dir

init-dev:
	python -m pip install -r requirements/core.txt -r requirements/dev.txt -r requirements/blog.txt --no-cache-dir
	cargo install typos-cli mlc

typo:
	typos automation docs

linkcheck:
	mlc docs

lint:
	ruff version
	ruff format automation --line-length 120
	ruff check automation --fix --line-length 120
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

check: typo linkcheck lint clean
