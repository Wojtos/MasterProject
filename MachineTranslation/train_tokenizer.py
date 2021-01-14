from tokenizers import ByteLevelBPETokenizer
import os
paths = ['./raw_datasets/cycl.txt']

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
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
