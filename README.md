# Build Toxic Text Classification App
![image1](image/toxic_.png)
## 1. Installment and Local Service

### 1.1 Requirements

```bash
$ pip install -r requirements.txt

```


### 1.2 Docker

```bash
$ docker pull khoav1371999/classify_toxic_text:0.0.1 
$ docker run -p 8081:30000 khoav1371999/classify_toxic_text:0.0.1 

```
### 1.3 Local Testing

Run ```client.py``` to test local API.

```bash
$ python3 client.py --save_dir toxic_classication.html --text_query your_text
```

## 2. Model

Utilized pretrained [DistilBERT](https://huggingface.co/transformers/v3.0.2/model_doc/distilbert.html) and incorporated two linear layers for the task of toxic text classification.

I use Jigsaw Toxic Comment Classification Challenge dataset to train and evaluate model. You can find details of the dataset [here](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data).


### 2.1 Model Architecture

![image3](image/architecture.png)

### 2.2 Model Specification

##### 2.2.1 Configuration

- Total Parameters: $68,728,321$
- Model Size: $262$ MB
- Optimizer: Adam
- Loss Function: Binary Cross Entropy
- Batch Size: $64$
- Linear Layer 1 Learning Rate: $5*10^{-4}$
- Linear Layer 2 Learning Rate: $1*10^{-5}$

##### 2.2.2 Train Loss

![image4](image/train_loss.png)

##### 2.2.3 Evaluation

![image5](image/confusion_matrix00.png)
