#!/bin/bash

source ../venv/bin/activate
python ../lib/transformers/examples/seq2seq/run_seq2seq.py \
    --model_name_or_path stas/tiny-wmt19-en-de \
    --tokenizer_name ../models/en_cycl_tokenizer \
    --do_train \
    --do_eval \
    --task translation_en_to_cycl \
    --source_lang en \
    --target_lang cycl \
    --train_file ../raw_datasets/train.json \
    --validation_file ../raw_datasets/validation.json \
    --output_dir ../models/en_cycl_$(date +%Y_%m_%d_%H_%M_%S) \
    --per_device_train_batch_size=64 \
    --per_device_eval_batch_size=64 \
    --overwrite_output_dir \
    --predict_with_generate
