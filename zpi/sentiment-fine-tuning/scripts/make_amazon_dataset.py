import pandas as pd
import os
import re
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

AMAZON_PATH = "data/amazon_reviews_cellphones.csv"
df_amazon = pd.read_csv(AMAZON_PATH, usecols=['body', 'rating'])
df_amazon.body.astype(str)
df_amazon['lengths'] = df_amazon['body'].apply(lambda x: len(str(x).split()))
df_amazon = df_amazon[df_amazon['lengths'] < 64]
df_amazon = df_amazon[df_amazon['lengths'] > 2]

# rename columns
df_amazon.rename(columns={'body': 'review'}, inplace=True)

df_amazon.reset_index(inplace=True, drop=True)
# df_amazon.head()

MODEL_NAME = 'xlm-roberta-base'
MODELS_FOLDER = '../sentiment-narwos-models'
FT_MODEL_PATH = os.path.join(MODELS_FOLDER, 'best_xlm_roberta.bin')


tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=3)

def cleanup_text(text: str) -> str:
    # Lowercase the text
    text = str(text).lower()
    
    # Remove newlines
    text = re.sub(r'\n+', ' ', text)
    
    # Remove unknown signs, but keep dots, commas, question marks, exclamation marks and hashtags
    text = re.sub(r'[^a-ząćęłńóśźż\s.,!?()\'\"]|\-(?!\w)|(?<!\w)\-', '', text)
    text = re.sub(r'([?!.,])\1+', r'\1', text)
    
    text = re.sub(r'(?<![a-z0-9])-|-(?![a-z0-9])', '', text)
    text = re.sub(r'([\'"])([^\1]*)\1', r'\2', text)
    text = re.sub(r'(?<!\w)([\'"])([^\1]*)\b\1', r'\2', text)
    text = re.sub(r'\((?!\s*\))|(?<!\()\s*\)', '', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r' {2,}', ' ', text)
    
    return text.strip()


def predict(text):
    encoded_input = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=64)
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = torch.softmax(torch.from_numpy(scores), dim=-1)
    return np.argmax(scores.detach().numpy())


df_amazon['review'] = df_amazon['review'].apply(cleanup_text)
df_amazon['review'] = df_amazon['review'].astype(str)
df_amazon['preds'] = df_amazon['review'].apply(predict)


df_amazon.to_csv('data/amazon_preds.csv', index=False)
print('done')
