#!/bin/bash

source venv/bin/activate
python ./lib/transformers/examples/language-modeling/run_mlm.py \
        --model_type bert \
        --train_file ./raw_datasets/cycl.txt \
        --validation_file ./raw_datasets/cycl-validation.txt \
        --tokenizer_name ./cyclberto \
        --line_by_line \
        --do_train \
        --do_eval \
        --output_dir bert \
