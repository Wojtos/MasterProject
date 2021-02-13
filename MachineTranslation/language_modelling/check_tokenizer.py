from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing
import os.path
import sys
ROOT_DIRECTORY = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(ROOT_DIRECTORY)

tokenizer = ByteLevelBPETokenizer(
     os.path.join(ROOT_DIRECTORY, "models/en_cycl_tokenizer/vocab.json"),
     os.path.join(ROOT_DIRECTORY, "models/en_cycl_tokenizer/merges.txt"),
)
tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)
tokenizer.enable_truncation(max_length=512)
token_to_encode = "(() ((#$isa #$McCoyTyner-Musician #$Individual)))"
encoded_token = tokenizer.encode(token_to_encode)
print(encoded_token)
print(encoded_token.tokens)

token_to_encode = "Pair of scissors is marketed as office product."
encoded_token = tokenizer.encode(token_to_encode)
print(encoded_token)
print(encoded_token.tokens)
