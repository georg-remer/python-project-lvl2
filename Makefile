install:
	poetry install

selfcheck:
	poetry check

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --cov=gendiff tests

check: selfcheck lint test

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl