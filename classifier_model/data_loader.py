from datasets import load_dataset
from torch.utils.data import DataLoader
from transformers import DataCollatorWithPadding

from config import CONFIG
from tokenizer import tokenizer

data_files = {"train": "train.csv"}
trainset = load_dataset("data", data_files=data_files)

dataset = trainset['train'].train_test_split(test_size=0.1, seed=0)
dataset = dataset.rename_column("toxic", "label")

def preprocess_function(examples):
    """
    Preprocess the given examples.

    Args:
        examples (dict): The examples to preprocess
        
    Returns:
        dict: The preprocessed examples
    """
    return tokenizer(examples["comment_text"], max_length=512, padding=True, truncation=True)

tokenized_dataset = dataset.map(preprocess_function, batched=True)
tokenized_dataset = tokenized_dataset.remove_columns(['id', 
                                                        'comment_text',
                                                        'severe_toxic',
                                                        'obscene',
                                                        'threat',
                                                        'insult',
                                                        'identity_hate'])

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

train_dataloader = DataLoader(
    tokenized_dataset["train"], batch_size=CONFIG.BATCH_SIZE, collate_fn=data_collator
)

eval_dataloader = DataLoader(
    tokenized_dataset["test"], batch_size=CONFIG.BATCH_SIZE, collate_fn=data_collator
)
