#!/bin/bash

CUDA_LAUNCH_BLOCKING=1
source ../venv/bin/activate
python ../language_modelling/train_tokenizer.py --name 32128_tokenizer --vocab_size 32128
python run_seq2seq.py \
    --model_name_or_path t5-small \
    --config_name ../models/t5_small_config.json \
    --tokenizer_name ../models/32128_tokenizer \
    --do_train \
    --do_eval \
    --task translation_en_to_cycl \
    --source_lang en \
    --target_lang cycl \
    --train_file ../raw_datasets/train.json \
    --validation_file ../raw_datasets/validation.json \
    --output_dir ../models/en_cycl_t5_small_transfer_learning \
    --per_device_train_batch_size=64 \
    --per_device_eval_batch_size=8 \
    --overwrite_output_dir \
    --predict_with_generate \
    --pad_to_max_length \
    --max_source_length 128 \
    --num_train_epochs 3
    # --max_train_samples 1 \
    # --max_val_samples 1
