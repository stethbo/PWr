import os
import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the fine-tuned model
MODEL_PATH = os.path.join('..', 'setniment-trained-models', 'checkpoint-2500')
MODEL_NAME = 'xlm-roberta-base'

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)



# Load the test data
DATA_PATH = os.path.join('data','data_labeled_remapped.csv')
df = pd.read_csv(DATA_PATH)

def predict(content):
    print(model(**tokenizer(content, return_tensors="pt")).logits)
    return torch.argmax(model(**tokenizer(content, return_tensors="pt")).logits).item()

df['label'] = df['label'].astype(int)
df['content'] = df['content'].astype(str)
df['pred'] = df['content'].apply(predict)

df.to_excel('data/test_results.xlsx', index=False)
