from tokenizers import ByteLevelBPETokenizer
import os

from transformers import RobertaConfig, RobertaTokenizerFast

paths = ['./raw_datasets/cycl.txt']

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=52_000, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

model_path = './cyclberto'
if not os.path.exists(model_path):
    os.mkdir(model_path)
tokenizer.save_model(model_path)

config = RobertaConfig(
    vocab_size=52_000
)

tokenizer = RobertaTokenizerFast.from_pretrained(model_path, max_len=512)
tokenizer.save_pretrained(model_path)
config.save_pretrained(model_path)
