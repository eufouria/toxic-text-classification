from loguru import logger
from sklearn.metrics import classification_report, roc_auc_score
import os
import torch
from torch import nn, optim
import warnings
warnings.filterwarnings("ignore")

from config import CONFIG
from data_loader import eval_dataloader, train_dataloader
from api.model import BertClassifier

device = torch.device("mps" if torch.backends.mps.is_built() else "cpu")
logger.info(f"Device: {device}")

classifier = BertClassifier()

# First, turn off the gradient for all parameters.
for param in classifier.parameters():
    param.requires_grad = False
# Then, turn on the gradient for classifier layer1.
for param in classifier.linear1.parameters():
    param.requires_grad = True
# Finally, turn on the gradient for classifier layer2.
for param in classifier.linear2.parameters():
    param.requires_grad = True

# optimizer
optimizer = optim.Adam([
    {'params': classifier.linear1.parameters(), 'lr': 5e-4},
    {'params': classifier.linear2.parameters(), 'lr': 1e-5}
])

# loss function
loss_function = nn.BCELoss()
epochs = CONFIG.TRAIN_EPOCHS


# send network to GPU
classifier.to(device)
train_losses, eval_losses = [], []

for epoch in range(epochs):
    all_loss = 0
    for idx, batch in enumerate(train_dataloader):
        if idx % 100 == 0:
            logger.info(f"Epoch {epoch}/{epochs} Step: {idx}/{len(train_dataloader)} \
                         Train Loss: {all_loss}")
        batch_loss = 0
        classifier.zero_grad()
        input_ids = batch.input_ids.to(device)
        attention_mask = batch.attention_mask.to(device)
        label_ids = batch.labels.unsqueeze(1).float().to(device)
        out = classifier(input_ids, attention_mask)
        batch_loss = loss_function(out, label_ids)
        batch_loss.backward()
        optimizer.step()
        all_loss += batch_loss.item()


    logger.info(f"Epoch {epoch} loss: {all_loss}")
    labels, predict, predict_score = [], [], []
    with torch.no_grad():
        for batch in eval_dataloader:

            input_ids = batch.input_ids.to(device)
            attention_mask = batch.attention_mask.to(device)
            label_ids = batch.labels.unsqueeze(1).to(device)
            score = classifier(input_ids, attention_mask)
            pred = score.round()
            predict_score += list(score.cpu().numpy())
            predict += list(pred.cpu().numpy())
            labels += list(label_ids.cpu().numpy())

    logger.info(f"Epoch {epoch} AUC: {roc_auc_score(labels, predict_score)}")
    logger.info(f"Epoch {epoch} \n {classification_report(labels, predict)}")

    MODEL_PATH = os.path.join(CONFIG.MODEL_FOLDER, f"tranfer_distilrobert_clf_1mil_chkpt{epoch}.pt")
    torch.save(classifier.state_dict(), MODEL_PATH)
    logger.info(f"Model successfully saved in {MODEL_PATH}!")
