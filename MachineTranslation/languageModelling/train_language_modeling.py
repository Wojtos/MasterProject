from transformers import RobertaConfig, RobertaForMaskedLM, RobertaTokenizerFast, LineByLineTextDataset, \
    Trainer, TrainingArguments, DataCollatorForLanguageModeling

config = RobertaConfig(
    vocab_size=52_000,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1,
)

tokenizer = RobertaTokenizerFast.from_pretrained("../models/cyclberto", max_len=512)
model = RobertaForMaskedLM(config=config)


dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path="../raw_datasets/cycl.txt",
    block_size=128,
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

training_args = TrainingArguments(
    output_dir="../models/cyclberto",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=64,
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

trainer.train()

trainer.save_model("../models/cyclberto")
