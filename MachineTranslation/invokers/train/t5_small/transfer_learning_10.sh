#!/bin/bash

CUDA_LAUNCH_BLOCKING=1
source ${MAIN_DIRECTORY_PATH}/venv/bin/activate
python ${MAIN_DIRECTORY_PATH}/language_modelling/train_tokenizer.py --name 32128_tokenizer --vocab_size 32128
python ${MAIN_DIRECTORY_PATH}/invokers/run_seq2seq.py \
    --model_name_or_path ${MAIN_DIRECTORY_PATH}/models/t5_small_transfer_learning_3 \
    --config_name ${MAIN_DIRECTORY_PATH}/configs/t5_small.json \
    --tokenizer_name ${MAIN_DIRECTORY_PATH}/models/32128_tokenizer \
    --$1 \
    --distributed_training \
    --task translation_en_to_cycl \
    --source_lang en \
    --target_lang cycl \
    --train_file ${MAIN_DIRECTORY_PATH}/raw_datasets/train.json \
    --validation_file ${MAIN_DIRECTORY_PATH}/raw_datasets/validation.json \
    --output_dir ${MAIN_DIRECTORY_PATH}/models/t5_small_transfer_learning_10 \
    --per_device_train_batch_size=64 \
    --per_device_eval_batch_size=64 \
    --overwrite_output_dir \
    --predict_with_generate \
    --pad_to_max_length \
    --max_source_length 128 \
    --num_train_epochs 10