import torch
import re
import os
import logging
import pandas as pd
from copy import deepcopy   

from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from transformers import (AutoTokenizer, AutoModelForSequenceClassification, 
                          Trainer, TrainingArguments, TrainerCallback)


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

MODEL_NAME = 'xlm-roberta-base'
DATA_PATH = os.path.join('data','data_labeled_remapped.csv')
TEXT_COLUMN = 'content'
LABEL_COLUMN = 'label'
NUM_LABELS = 3
SPLIT = 0.8

# Training arguments
EPOCHS = 24
BATCH_SIZE = 64
WARMPUP_STEPS = 500
WEIGHT_DECAY = 0.01
LEARNING_RATE = 1e-5
OUTPUT_DIR = 'fine_tuned_models'
SAVE_STEPS = 30
SEQUENCE_MAX_LENGTH = 64

class MyDataset(torch.utils.data.Dataset):

    def __init__(self, contents, labels, tokenizer):
        self.contents    = contents
        self.labels = labels
        self.tokenizer  = tokenizer
        self.max_len    = SEQUENCE_MAX_LENGTH
  
    def __len__(self):
        return len(self.contents)
  
    def __getitem__(self, index):
        content = str(self.contents[index])
        label = self.labels[index]

        encoded_review = self.tokenizer.encode_plus(
            content,
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
            'labels': torch.eye(NUM_LABELS)[label - 1]
        }


class CustomCallback(TrainerCallback):
    
    def __init__(self, trainer) -> None:
        super().__init__()
        self._trainer = trainer
    
    def on_epoch_end(self, args, state, control, **kwargs):
        if control.should_evaluate:
            control_copy = deepcopy(control)
            self._trainer.evaluate(eval_dataset=self._trainer.train_dataset, metric_key_prefix="train")
            logger.info(f"Epoch {state.epoch} - Training loss: {state.metrics['train_loss']}")
            return control_copy


def read_data(path):
    if path.endswith('.csv'):
        df = pd.read_csv(path)
    elif path.endswith('.xlsx'):
        df = pd.read_excel(path)
    else:
        raise Exception('Unsupported file format')
    return df

def convert_sentiment(sentiment):
    return 1 if sentiment == 'Positive' else 0


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


def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='weighted')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }


if __name__ == "__main__":
    dataset = read_data(DATA_PATH)
    dataset[TEXT_COLUMN] = dataset[TEXT_COLUMN].apply(cleanup_text)
    dataset[LABEL_COLUMN] = dataset[LABEL_COLUMN].apply(lambda x: x - 1)

    logger.info(f'Dataset loaded successfully, sample records:')
    logger.info(f'\n{dataset.head()}\n')
    dataset.dropna(inplace=True)

    train_set = dataset[:int(len(dataset) * SPLIT)]
    test_set = dataset[int(len(dataset) * SPLIT):]

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    train_dataset = MyDataset(
        contents    = train_set[TEXT_COLUMN].tolist(),
        labels = train_set[LABEL_COLUMN].tolist(),
        tokenizer  = tokenizer,
    )

    test_dataset = MyDataset(
        contents    = test_set[TEXT_COLUMN].tolist(),
        labels = test_set[LABEL_COLUMN].tolist(),
        tokenizer  = tokenizer,
    )
    logger.info(f'Dataset created successfully!')
    logger.info(f'train size: {len(train_dataset)}, test size: {len(test_dataset)}')


    # Create DataLoader for train/validation sets.
    train_set_dataloader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size  = BATCH_SIZE,
        num_workers = 4
    )

    valid_set_dataloader = torch.utils.data.DataLoader(
        test_dataset,
        batch_size  = BATCH_SIZE,
        num_workers = 4
    )

    # Get one batch as example.
    train_data = next(iter(train_set_dataloader))
    valid_data = next(iter(valid_set_dataloader))

    # Print the output sizes.
    logger.info(f'Sizes of taining data batches:')
    logger.info(f'{train_data["input_ids"].size()}, {valid_data["input_ids"].size()}')

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME,
                                                               num_labels=NUM_LABELS)

    for i, (name, param) in enumerate(model.named_parameters()):
        if name.startswith('classifier'):
            logger.info(f'Classifier layer: {name}, number: {i}')
            param.requires_grad = True
        else:
            param.requires_grad = False

    logger.info(f'Model set up successfully: {model.name_or_path}')

    training_args = TrainingArguments(
        output_dir                  = OUTPUT_DIR,
        num_train_epochs            = EPOCHS,
        per_device_train_batch_size = 128,
        per_device_eval_batch_size  = 64,
        learning_rate               = LEARNING_RATE,
        warmup_steps                = WARMPUP_STEPS,
        weight_decay                = WEIGHT_DECAY,
        save_steps                  = SAVE_STEPS,
        save_strategy               = "epoch",
        evaluation_strategy         = "steps"
    )
    logger.info(f'Training arguments set up successfully.')

    trainer = Trainer(
        model           = model,
        args            = training_args,
        train_dataset   = train_dataset,
        eval_dataset    = test_dataset,
        compute_metrics = compute_metrics,
        callbacks       = [CustomCallback()]
    )

    

    trainer.add_callback(CustomCallback(trainer)) 
    logger.info('Trainer set up successfully')

    logger.info('Training started...')
    # trainer.train()
