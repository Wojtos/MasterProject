#!/bin/bash

CUDA_LAUNCH_BLOCKING=1
source ../venv/bin/activate
python ../language_modelling/train_tokenizer.py
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
    --predict_with_generate \
    --pad_to_max_length \
    --max_source_length 128
    # --max_train_samples 1 \
    # --max_val_samples 1
