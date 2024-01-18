import os

class CONFIG:
    DEVICE = "cpu"
    MODEL_PATH = os.path.join(os.path.dirname(__file__),\
            "classifier_model/my_awesome_model/finetuned_bert_1m.pt")
    TOXIC_THRESHOLD = 0.45
