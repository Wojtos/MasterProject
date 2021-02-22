from transformers import AutoModelWithLMHead, RobertaTokenizerFast

model_path = "../models/en_cycl_2021_02_22_11_41_01/checkpoint-10000"

model = AutoModelWithLMHead.from_pretrained(model_path)
tokenizer = RobertaTokenizerFast.from_pretrained(model_path, max_len=512)

inputs = tokenizer.encode("Pair of scissors is marketed as office product.", return_tensors="pt")
outputs = model.generate(inputs)

print(tokenizer.decode(outputs[0]))
