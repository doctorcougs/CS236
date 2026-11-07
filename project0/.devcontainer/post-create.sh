#!/bin/sh
set -e

# Install the package
pip install --user --editable ".[dev]"

# Install pre-commit
pre-commit install
