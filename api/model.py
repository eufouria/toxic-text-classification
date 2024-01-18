import torch
from classifier_model.model import BertClassifier
from config import CONFIG

class FineTunedBertClassifier:
    def __init__(self):
        self.name = "finetuned_distilbert"
        self.model_path = CONFIG.MODEL_PATH
        self.device = CONFIG.DEVICE
        self.classifier = _load_saved_model(self.model_path, self.device)
    
    def score2label(self, score):
        return int(score >= CONFIG.TOXIC_THRESHOLD)   

def _load_saved_model(PATH, device):
    device = torch.device(device)
    model = BertClassifier()
    model.load_state_dict(torch.load(PATH, map_location=device))
    return model
