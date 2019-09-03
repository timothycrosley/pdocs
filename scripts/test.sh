#!/bin/bash -xe

# ./scripts/lint.sh
poetry run pytest --cov=pdocs --cov=tests --cov-report=term-missing ${@} --cov-report html tests --capture=no --color=yes
