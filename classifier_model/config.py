class CONFIG:
    BATCH_SIZE = 64
    MAX_LENGTH = 512
    EVAL_SIZE = 0.05
    CLASS_WEIGHT = [1, 1/9]
    TRAIN_EPOCHS = 5
    MODEL_FOLDER = "./my_awesome_model/"
    DEVICE = "cpu"
    TOXIC_THRESHOLD = 0.45
    BUCKET_NAME = 'toxic-model'
    SOURCE_BLOB_NAME = 'finetuned_bert_1m.pt'
    DESTINATION_FILE_NAME = 'finetuned_bert_1m.pt'