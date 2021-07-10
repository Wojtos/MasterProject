import subprocess
import re
import os.path
import sys

ROOT_DIRECTORY = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(ROOT_DIRECTORY)
import json


def compute_lines_by_predicate(lines):
    lines_by_predicate = {}
    for line in lines:
        # print(line)
        # predicate = line.split('{"cycl": "(() ((')[1].split()[0]
        predicate = '#$' + line.split('#$')[1].split()[0]
        if predicate not in lines_by_predicate:
            lines_by_predicate[predicate] = []
        lines_by_predicate[predicate].append(line)
    return lines_by_predicate


def decrease_dataset_size(lines_by_predicate, target_size):
    lines_to_return = []
    iteration = 0
    while len(lines_to_return) < target_size:
        for predicate, lines in lines_by_predicate.items():
            if len(lines) > iteration:
                lines_to_return.append(lines[iteration])
            if len(lines_to_return) >= target_size:
                return lines_to_return
        iteration += 1

def decrease_size_and_save_file(
        original_file_path,
        target_file_path,
        target_size
):
    original_file = open(original_file_path)
    lines = original_file.readlines()
    lines_by_predicate = compute_lines_by_predicate(lines)
    print(len(lines_by_predicate))
    lines_to_return = decrease_dataset_size(lines_by_predicate, target_size)
    print(len(lines_to_return))
    target_file = open(target_file_path, 'w')
    target_file.writelines(lines_to_return)

decrease_size_and_save_file(
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/train.json'),
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/train-smaller.json'),
    100000
)

decrease_size_and_save_file(
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/validation.json'),
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/validation-smaller.json'),
    10000
)
