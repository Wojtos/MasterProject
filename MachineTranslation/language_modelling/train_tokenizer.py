from tokenizers import ByteLevelBPETokenizer
import os

from transformers import RobertaConfig, RobertaTokenizerFast

paths = [
    '../raw_datasets/cycl-filtered.txt',
    '../raw_datasets/english-filtered.txt',
]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=42024, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

model_path = '../models/en_cycl_tokenizer'
if not os.path.exists(model_path):
    os.mkdir(model_path)
tokenizer.save_model(model_path)

config = RobertaConfig(
    vocab_size=42024
)

tokenizer = RobertaTokenizerFast.from_pretrained(model_path, max_len=512)
tokenizer.save_pretrained(model_path)
config.save_pretrained(model_path)
