#!/bin/sh

if [ $# -ne 1 ]; then
    echo "usage: sh config_test.sh <test-name-or-k-expression>"
    exit 1
fi

printf '[pytest]\naddopts = -k "%s"\n' "$1" > pytest.ini
pip install ".[classroom]"
