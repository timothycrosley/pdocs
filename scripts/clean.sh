#!/bin/bash -xe

poetry run isort --recursive pdocs tests/
poetry run black pdocs/ tests/ -l 100 --exclude malformed
