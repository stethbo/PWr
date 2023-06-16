import torch
import re
import logging
import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

MODEL_NAME = 'xlm-roberta-base'
DATA_PATH = '/home/stefan/PWr/ZPI/narwos-nlp/files/imbd_movie_reviews/MovieReviewTrainingDatabase.csv'
SPLIT = 0.8


class MyDataset(torch.utils.data.Dataset):

    def __init__(self, reviews, sentiments, tokenizer):
        self.reviews    = reviews
        self.sentiments = sentiments
        self.tokenizer  = tokenizer
        self.max_len    = tokenizer.model_max_length
  
    def __len__(self):
        return len(self.reviews)
  
    def __getitem__(self, index):
        review = str(self.reviews[index])
        sentiments = self.sentiments[index]

        encoded_review = self.tokenizer.encode_plus(
            review,
            add_special_tokens    = True,
            max_length            = self.max_len,
            return_token_type_ids = False,
            return_attention_mask = True,
            return_tensors        = "pt",
            padding               = "max_length",
            truncation            = True
        )

        return {
            'input_ids': encoded_review['input_ids'][0],
            'attention_mask': encoded_review['attention_mask'][0],
            'labels': torch.tensor(sentiments, dtype=torch.long)
        }


def convert_sentiment(sentiment):
    return 1 if sentiment == 'Positive' else 0


def cleanup_text(text):
    # Lowercase the text
    text = text.lower()
    
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


def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='binary')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }



if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    dataset = pd.DataFrame()
    dataset['review'] = df['review'].apply(cleanup_text)
    dataset['label'] = df['sentiment'].apply(convert_sentiment)


    train_set = dataset[:int(len(dataset) * SPLIT)]
    test_set = dataset[int(len(dataset) * SPLIT):]
    print(len(train_set), len(test_set))

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    train_dataset = MyDataset(
        reviews    = train_set.review.tolist(),
        sentiments = train_set.label.tolist(),
        tokenizer  = tokenizer,
    )

    test_dataset = MyDataset(
        reviews    = test_set.review.tolist(),
        sentiments = test_set.label.tolist(),
        tokenizer  = tokenizer,
    )


    # Create DataLoader for train/validation sets.
    train_set_dataloader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size  = 16,
        num_workers = 4
    )

    valid_set_dataloader = torch.utils.data.DataLoader(
        test_dataset,
        batch_size  = 16,
        num_workers = 4
    )

    # Get one batch as example.
    train_data = next(iter(train_set_dataloader))
    valid_data = next(iter(valid_set_dataloader))

    # Print the output sizes.
    print( train_data["input_ids"].size(), valid_data["input_ids"].size() )

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

    for i, (name, param) in enumerate(model.named_parameters()):
        if name.startswith('classifier'):
            print(f'Classifier layer: {name}, number: {i}')
            param.requires_grad = True
        else:
            param.requires_grad = False


    training_args = TrainingArguments(
        output_dir                  = "./sentiment-analysis",
        num_train_epochs            = 1,
        per_device_train_batch_size = 128,
        per_device_eval_batch_size  = 64,
        warmup_steps                = 500,
        weight_decay                = 0.01,
        save_strategy               = "epoch",
        evaluation_strategy         = "steps"
    )

    trainer = Trainer(
        model           = model,
        args            = training_args,
        train_dataset   = train_dataset,
        eval_dataset    = test_dataset,
        compute_metrics = compute_metrics
    )

    trainer.train()
