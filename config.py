import os

class CONFIG:
    DEVICE = "cpu"
    TOXIC_THRESHOLD = 0.45
    BUCKET_NAME = 'toxic-model'
    SOURCE_BLOB_NAME = 'finetuned_bert_1m.pt'
    DESTINATION_FILE_NAME = 'finetuned_bert_1m.pt'
