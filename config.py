import os

class CONFIG:
    DEVICE = "cpu"
    TOXIC_THRESHOLD = 0.45
    BUCKET_NAME = 'toxic-model'
    SOURCE_BLOB_NAME = 'finetuned_bert_1m.pt'
    DESTINATION_FILE_NAME = os.path.join(os.path.dirname(__file__),\
            "classifier_model/my_awesome_model/finetuned_bert_1m.pt")
