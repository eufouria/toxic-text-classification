from data_loader import eval_dataloader
from model import BertClassifier
import torch
from torch import nn

classifier = BertClassifier()
loss_function = nn.BCELoss()

eval_loss = []
with torch.no_grad():
    for i in range(10):
        
        classifier = BertClassifier()
        classifier.load_state_dict(torch.load(f"my_awesome_model/tranfer_distilrobert_clf_1mil_chkpt{i}.pt", map_location="cpu"))
        
        all_loss = 0
        for batch in eval_dataloader:
            batch_loss = 0
            input_ids = batch.input_ids
            attention_mask = batch.attention_mask
            label_ids = batch.labels.unsqueeze(1)
            score = classifier(input_ids, attention_mask)
            
            batch_loss = loss_function(score, label_ids)
            all_loss += batch_loss.item()
        eval_loss.append(all_loss)
print(eval_loss)