#!/bin/sh

set -e

./bin/coverage run \
    --source src/yafowil/widget/chosen \
    --omit src/yafowil/widget/chosen/example.py \
    -m yafowil.widget.chosen.tests
./bin/coverage report
./bin/coverage html
