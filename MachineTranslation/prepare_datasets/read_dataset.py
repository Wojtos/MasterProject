import os.path
import sys
ROOT_DIRECTORY = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(ROOT_DIRECTORY)

def read_dataset(dataset_path):
    binary_file = open(dataset_path, 'rb')
    bytes = binary_file.read(1024 * 1024 * 1024)
    line_endings_indexes = [i for (i, byte) in enumerate(bytes) if byte == 10]
    strings = [bytes[0 if i == 0 else line_endings_indexes[i - 1] + 1:line_endings_indexes[i]].decode()
               for (i, index) in enumerate(line_endings_indexes)]
    return strings
