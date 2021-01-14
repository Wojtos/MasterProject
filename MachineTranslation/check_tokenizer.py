from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing


tokenizer = ByteLevelBPETokenizer(
    "./cyclberto/vocab.json",
    "./cyclberto/merges.txt",
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
