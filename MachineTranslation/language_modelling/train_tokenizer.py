from tokenizers import ByteLevelBPETokenizer
import os
from transformers import RobertaConfig, RobertaTokenizerFast
import argparse

paths = [
    '../raw_datasets/cycl-filtered.txt',
    '../raw_datasets/english-filtered.txt',
]

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str)
parser.add_argument('--vocab_size', type=int)
args = parser.parse_args()

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=args.vocab_size, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

model_path = f'../models/{args.name}'
if not os.path.exists(model_path):
    os.mkdir(model_path)
tokenizer.save_model(model_path)

config = RobertaConfig(
    vocab_size=args.vocab_size
)

tokenizer = RobertaTokenizerFast.from_pretrained(model_path, max_len=512)
tokenizer.save_pretrained(model_path)
config.save_pretrained(model_path)
