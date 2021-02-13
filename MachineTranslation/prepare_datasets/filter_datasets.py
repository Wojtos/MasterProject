import subprocess
import re
import os.path
import sys
ROOT_DIRECTORY = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(ROOT_DIRECTORY)
from prepare_datasets.read_dataset import read_dataset

UNALLOWED_ENGLISH_SUBSTRINGS = ['#', '$', ':', '?', '{', '}', '[', ']', '(', ')', '\\', 'Mt', 'Fn', 'LF', 'CycL', 'no.']
UNALLOWED_CYCL_SUBSTRINGS = ['#$functionalInArgs']
MAX_SENTENCE_SIZE = 100

def check_pair(cycl_sentence, english_sentence):
    return not contains_unallowed_english_substrings(english_sentence) and \
           not contains_unallowed_cycl_substrings(cycl_sentence) and \
           not exclude_pair_with_too_big_len_difference(cycl_sentence, english_sentence)


def contains_unallowed_english_substrings(english_sentence):
    for sign in UNALLOWED_ENGLISH_SUBSTRINGS:
        if sign in english_sentence:
            return True
    return False


def contains_unallowed_cycl_substrings(cycl_sentence):
    for sign in UNALLOWED_CYCL_SUBSTRINGS:
        if sign in cycl_sentence:
            return True
    return False


def exclude_pair_with_too_big_len_difference(cycl_sentence, english_sentence):
    len_cycl = len(cycl_sentence)
    len_english = len(english_sentence)
    return len_cycl * 2 < len_english or len_english * 2 < len_cycl



def filter_datasets(cycl_dataset_path, english_dataset_path):
    # cycl_file = open(cycl_dataset_path, 'r')
    # english_file = open(english_dataset_path, 'r')

    cycl_lines = read_dataset(cycl_dataset_path)
    english_lines = read_dataset(english_dataset_path)

    # cycl_lines = [line.rstrip('\n\xa0') for line in cycl_file if line]
    # english_lines = [line.rstrip('\n\xa0') for line in english_file if line]

    # cycl_lines = cycl_file.read().split('\n')
    # english_lines = english_file.read().split('\n')

    print(len(cycl_lines))
    print(len(english_lines))

    return [(cycl_sentence, english_sentence) for cycl_sentence, english_sentence
            in zip(cycl_lines, english_lines) if check_pair(cycl_sentence, english_sentence)]


def save_dataset(dataset, dataset_path):
    file = open(dataset_path, 'w')
    lines = '\n'.join(dataset)
    file.writelines(lines)


def normailize_english_dataset(english_dataset):
    return [line.capitalize() + '.' for line in english_dataset]


def filter_and_save_datasets(
        cycl_original_dataset_path,
        english_original_dataset_path,
        cycl_target_dataset_path,
        english_target_dataset_path
    ):
    filtered_datasets = filter_datasets(
        cycl_original_dataset_path,
        english_original_dataset_path,
    )
    print(len(filtered_datasets))
    cycl_target_lines = list(map(lambda x: x[0], filtered_datasets))
    english_target_lines = list(map(lambda x: x[1], filtered_datasets))
    english_target_lines = normailize_english_dataset(english_target_lines)
    save_dataset(cycl_target_lines, cycl_target_dataset_path)
    save_dataset(english_target_lines, english_target_dataset_path)


filter_and_save_datasets(
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/cycl.txt'),
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/english.txt'),
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/cycl-filtered.txt'),
    os.path.join(ROOT_DIRECTORY, 'raw_datasets/english-filtered.txt'),
)


def count_lines_in_unix(dataset_path, starting_line=0):
    first_command = ['tail', '-n', f'+{starting_line + 1}', dataset_path]
    first_process = subprocess.Popen(first_command, stdout=subprocess.PIPE)
    second_command = ['wc', '-l']
    second_process = subprocess.Popen(second_command, stdout=subprocess.PIPE, stdin=first_process.stdout)

    process_result = str(second_process.stdout.read())
    process_result = int(re.findall('\d+', process_result)[0])
    return process_result


def compute_line_in_unix(dataset_path, starting_line=0):
    first_command = ['tail', '-n', f'+{starting_line + 1}', dataset_path]
    first_process = subprocess.Popen(first_command, stdout=subprocess.PIPE)

    second_command = ['head', '-n' '1']
    second_process = subprocess.Popen(second_command, stdout=subprocess.PIPE, stdin=first_process.stdout)

    process_result = str(second_process.stdout.read())
    first_opening_parentheses = [m.start() for m in re.finditer('\(', process_result)][0]
    last_closing_parentheses = [m.start() for m in re.finditer('\)', process_result)][-1]
    process_result = str(process_result[first_opening_parentheses:last_closing_parentheses+1])
    return process_result


def find_line_with_wrong_char(dataset_path):
    file = open(dataset_path, 'r')
    lines = file.readlines()
    python_lines_count = len(lines)
    unix_lines_count = count_lines_in_unix(dataset_path)
    difference_lines_count = python_lines_count - unix_lines_count
    for index, line in enumerate(lines):
        new_unix_lines_count = count_lines_in_unix(dataset_path, index)
        new_difference_lines_count = python_lines_count - index - new_unix_lines_count
        if new_difference_lines_count != difference_lines_count:
            print(index)
            print(line)
            print(difference_lines_count)
            print(new_difference_lines_count)
            break



# find_line_with_wrong_char('../raw_datasets/cycl-validation.txt')


# dataset_path = '../raw_datasets/cycl-validation.txt'
# file = open(dataset_path, 'r')
# lines = file.readlines()
# python_lines_count = len(lines)
# unix_lines_count = count_lines_in_unix(dataset_path)
# dif1 = python_lines_count - unix_lines_count
# dif2 = count_lines_in_unix(dataset_path, starting_line=unix_lines_count)
# print(unix_lines_count)
# print(dif1)
# print(dif2)
# tmp = 79032
# dif3 = python_lines_count - tmp - count_lines_in_unix(dataset_path, starting_line=tmp)
# print(dif3)

def find_line_with_wrong_char_second(dataset_path):
    file = open(dataset_path, 'r')
    lines = file.readlines()
    print(len(lines))
    return
    for index, line in enumerate(lines):
        unix_line = compute_line_in_unix(dataset_path, index)
        line = line.replace('\n', '')
        unix_line = unix_line.replace('\\', '')
        if line != unix_line:
            print(index)
            print(line)
            print(unix_line)
            break

# find_line_with_wrong_char_second('../raw_datasets/cycl-wtf.txt')
# print(compute_line_in_unix('../raw_datasets/cycl-validation.txt'))
def first_line(dataset_path):
    file = open(dataset_path, 'r')
    lines = file.readlines()
    print(lines[0])
    print(lines[1])
    file_binary = open(dataset_path, 'r')
    first_lines = file_binary.read(500)
    indexes_10 = [i for i, byte in enumerate(first_lines) if ord(byte) == 10]
    indexes_32 = [i for i, byte in enumerate(first_lines) if ord(byte) == 32]
    for index in indexes_10:
        print(first_lines[index-2:index] + first_lines[index+1:index+3])
    print(indexes_10)
    print(indexes_32)
    # print(ord('\n'))


def count_real_cycl_lines(dataset_path):
    file = open(dataset_path, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(len(lines))
    lines = [line for line in lines if line]
    lines = [line for line in lines if line[:2] == '((']
    print(len(lines))

# count_real_cycl_lines('../raw_datasets/cycl.txt')


def count_real_english_lines(dataset_path):
    file = open(dataset_path, 'r')
    # lines = file.readlines()
    lines = file.read().split('\n')
    # print(len(lines))
    # lines = [line.strip() for line in lines]
    # print(len(lines))
    lines = [line for line in lines if line]
    lines = [line for line in lines if line[0] != ' ' and line[0] != '\n' and line[0] != '\t']
    print(len(lines))
    binary_file = open(dataset_path, 'rb')
    bytes = binary_file.read(500)
    line_endings = [(i, byte) for (i, byte) in enumerate(bytes) if byte == 10]
    print(line_endings)
    print(bytes[113])

def new_split(dataset_path):
    file = open(dataset_path, 'r')
    # lines = file.read().split('\n')
    # print(lines)
    # print(len(lines))

    binary_file = open(dataset_path, 'rb')
    bytes = binary_file.read(1024 * 1024 * 1024)
    line_endings = [(i, byte) for (i, byte) in enumerate(bytes) if byte == 10]
    print(len(line_endings))

# count_real_english_lines('../raw_datasets/english.txt')
# first_line('../raw_datasets/english-single.txt')
# new_split('../raw_datasets/cycl.txt')