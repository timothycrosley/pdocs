#!/bin/bash -xe

poetry run mypy --ignore-missing-imports pdocs/
poetry run isort --check --diff --recursive pdocs/ tests/
poetry run black --check -l 100 pdocs/ tests/ --exclude malformed
poetry run flake8 --max-line 100 --ignore F403,F401,W503 --exclude mitmproxy/contrib/*,test/mitmproxy/data/*,release/build/*,*malformed*
poetry run safety check
poetry run bandit -r pdocs
