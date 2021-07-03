#!/bin/bash

CUDA_LAUNCH_BLOCKING=1
source ${MAIN_DIRECTORY_PATH}/venv/bin/activate
python ${MAIN_DIRECTORY_PATH}/language_modelling/train_tokenizer.py --name 31232_tokenizer --vocab_size 31232
python ${MAIN_DIRECTORY_PATH}/invokers/run_seq2seq.py \
    --model_name_or_path ${MAIN_DIRECTORY_PATH}/models/wmt19_en_ru_transfer_learning_3 \
    --config_name ${MAIN_DIRECTORY_PATH}/configs/wmt19_en_ru.json \
    --tokenizer_name ${MAIN_DIRECTORY_PATH}/models/31232_tokenizer \
    --$1 \
    --task translation_en_to_cycl \
    --source_lang en \
    --target_lang cycl \
    --train_file ${MAIN_DIRECTORY_PATH}/raw_datasets/train.json \
    --validation_file ${MAIN_DIRECTORY_PATH}/raw_datasets/validation.json \
    --output_dir ${MAIN_DIRECTORY_PATH}/models/wmt19_en_ru_transfer_learning_10 \
    --per_device_train_batch_size=64 \
    --per_device_eval_batch_size=64 \
    --overwrite_output_dir \
    --predict_with_generate \
    --pad_to_max_length \
    --max_source_length 128 \
    --num_train_epochs 10