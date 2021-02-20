#!/bin/bash

virtualenv -p python ../venv
source ../venv/bin/activate
pip install -r ../requirements.txt
pip install -r ../lib/transformers/examples/seq2seq/requirements.txt
