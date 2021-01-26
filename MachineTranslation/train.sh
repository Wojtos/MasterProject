#!/bin/bash

source venv/bin/activate
python train_tokenizer.py
python train_language_modeling.py
