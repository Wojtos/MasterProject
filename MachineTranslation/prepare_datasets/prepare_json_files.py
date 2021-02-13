import json
import os.path
import sys
import random

ROOT_DIRECTORY = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(ROOT_DIRECTORY)

from prepare_datasets.read_dataset import read_dataset


def prepare_json_translation_files(
        cycl_original_dataset_path,
        english_original_dataset_path,
        training_joined_dataset_json_path,
        validation_joined_dataset_json_path,
        ratio=0.9
):
    cycl_dataset = read_dataset(cycl_original_dataset_path)
    english_dataset = read_dataset(english_original_dataset_path)
    assert len(cycl_dataset) == len(english_dataset)

    translation_size = len(cycl_dataset)

    indexes = list(range(translation_size))
    random.shuffle(indexes)
    boundary_index = int(translation_size * ratio)
    training_indexes = indexes[:boundary_index]
    validation_indexes = indexes[boundary_index + 1:]

    prepare_json_file(cycl_dataset, english_dataset, training_joined_dataset_json_path, training_indexes)
    prepare_json_file(cycl_dataset, english_dataset, validation_joined_dataset_json_path, validation_indexes)


def prepare_json_file(
        cycl_dataset,
        english_dataset,
        target_joined_dataset_json_path,
        indexes
):

    filtered_cycl_dataset = [cycl_dataset[i] for i in indexes]
    filtered_english_dataset = [english_dataset[i] for i in indexes]
    data = {}
    translation = data['translation'] = {}
    translation['cycl'] = filtered_cycl_dataset
    translation['en'] = filtered_english_dataset

    with open(target_joined_dataset_json_path, 'w') as outfile:
        json.dump(data, outfile)


prepare_json_translation_files(
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/cycl-filtered.txt'),
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/english-filtered.txt'),
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/train.json'),
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/validation.json'),
)
