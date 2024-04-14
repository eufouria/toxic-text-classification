import torch
from google.cloud import storage
from classifier_model.model import BertClassifier
from config import CONFIG

class FineTunedBertClassifier:
    def __init__(self):
        self.name = "finetuned_distilbert"
        # Download the model file from GCS
        _download_blob(CONFIG.BUCKET_NAME, CONFIG.SOURCE_BLOB_NAME, CONFIG.DESTINATION_FILE_NAME)
        self.model_path = CONFIG.DESTINATION_FILE_NAME
        self.device = CONFIG.DEVICE
        self.classifier = _load_saved_model(self.model_path, self.device)
    
    def score2label(self, score):
        return int(score >= CONFIG.TOXIC_THRESHOLD)   


def _download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

def _load_saved_model(PATH, device):
    device = torch.device(device)
    model = BertClassifier()
    model.load_state_dict(torch.load(PATH, map_location=device))
    return model
