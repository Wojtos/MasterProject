#!/bin/bash

virtualenv -p python venv
source venv/bin/activate
pip install -r requirements.txt
