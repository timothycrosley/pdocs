#!/bin/bash -xe

poetry run mypy --ignore-missing-imports pdocs/
poetry run isort --check --diff --recursive pdocs/ tests/
poetry run black --check -l 100 pdocs/ tests/ --exclude malformed
poetry run flake8 pdocs/ tests/ --max-line 100 --ignore F403,F401,W503,E203 --exclude mitmproxy/contrib/*,test/mitmproxy/data/*,release/build/*,*malformed*
poetry run safety check -i 51457
poetry run bandit -r pdocs
