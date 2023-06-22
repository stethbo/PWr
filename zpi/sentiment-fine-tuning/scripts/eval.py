import torch
import pandas as pd
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments)

from sentiment_fine_tuning import (compute_metrics, Trainer, DATA_PATH, MODEL_NAME,
                          cleanup_text, MyDataset, read_data, TEXT_COLUMN, LABEL_COLUMN,
                          NUM_LABELS)


CHECPOINT_PATH = "/home/stefan/PWr/uni/PWr/zpi/sentiment-fine-tuning/setniment-trained-models/checkpoint-2500"

# Load the checkpoint
model = AutoModelForSequenceClassification.from_pretrained(CHECPOINT_PATH, 
                                                           num_labels=NUM_LABELS,
                                                           ignore_mismatched_sizes=True)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

df = pd.read_csv(DATA_PATH)
df[TEXT_COLUMN] = df[TEXT_COLUMN].apply(cleanup_text)
df[LABEL_COLUMN] = df[LABEL_COLUMN].apply(lambda x: x - 1)

df.dropna(inplace=True)
test_set = df[int(len(df) * 0.8):]

# Make the test set ready
test_set_dataset = MyDataset(
    contents = test_set[TEXT_COLUMN].tolist(),
    labels = test_set[LABEL_COLUMN].tolist(),
    tokenizer  = tokenizer,
)

# training_args = TrainingArguments(
#     output_dir = "./sentiment-analysis",
#     do_predict = True
# )

# trainer = Trainer(
#     model           = model,
#     args            = training_args,
#     compute_metrics =compute_metrics,
# )

model.eval()
for row in test_set_dataset:
    print(row)
    X = row['input_ids'].unsqueeze(0)
    y = row['labels'].unsqueeze(0)
    outputs = model(X, labels=y)
    print(outputs)
    break


# trainer.predict(test_set_dataset)