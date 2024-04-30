from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel
from transformers import AutoTokenizer

from api.model import FineTunedBertClassifier

app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = FineTunedBertClassifier()

class ClassifyToxicTextResponse(BaseModel):
    toxic_score: float
    is_toxic: int

@app.post("/classify_text", response_model=ClassifyToxicTextResponse)
async def classify_text(text:str):
    """
    Classify the toxicity of the given text.
    
    Args:
        text (str): The text to classify
        
    Returns:
        dict: The toxic score and the label
    """
    inputs = tokenizer(text, max_length=512, padding='max_length', \
                       truncation=True, return_tensors='pt')
    toxic_score = model.classifier(**inputs).item()
    is_toxic = model.score2label(toxic_score)
    logger.info(f"User: {text}")
    response = ClassifyToxicTextResponse(toxic_score=toxic_score, is_toxic=is_toxic)
    return response
