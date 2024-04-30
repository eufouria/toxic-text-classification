import torch
from torch import nn
from transformers import DistilBertModel

class BertClassifier(nn.Module):
    """
    A class to represent a BERT classifier.

    Attributes:
        bert (transformers.DistilBertModel): The BERT model
        linear1 (torch.nn.Linear): The first linear layer
        linear2 (torch.nn.Linear): The second linear layer
    """
    def __init__(self):
        super(BertClassifier, self).__init__()
        self.bert = DistilBertModel.from_pretrained("distilbert-base-uncased")
        # BERT last hidden state size is 768
        self.linear1 = nn.Linear(768, 3072)
        self.linear2 = nn.Linear(3072, 1)

    def forward(self, input_ids, attention_mask):
        # get last_hidden_state
        vec = self.bert(input_ids, attention_mask).last_hidden_state
        # only get first token '[CLS]'
        vec = vec[:,0,:]
        x_bert = vec.view(-1, 768)
        x_l1 = torch.relu(self.linear1(x_bert))
        x_l2 = torch.sigmoid(self.linear2(x_l1))
        return x_l2
