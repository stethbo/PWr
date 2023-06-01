import logging
import yaml

CONFIG_FILE = 'config.yaml'
LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOGGER_LEVEL = 'INFO'

logging.basicConfig(
    level=LOGGER_LEVEL,
    format=LOGGING_FORMAT)

logger = logging.getLogger(__name__)

with open(CONFIG_FILE, 'r') as yaml_file:
    CONFIG = yaml.load(yaml_file, Loader=yaml.SafeLoader)
    logger.info('Configuration loaded successfully')

from sentence_transformers import SentenceTransformer, InputExample
from sentence_transformers import models, losses, evaluation
from torch.utils.data import DataLoader
import pandas as pd
import random
import os

logger.info('All needed libraries loaded successfully')

SEED = CONFIG.get('seed')

DATA_FILE = CONFIG.get('datafile')
MODEL_NAME = CONFIG.get('model')
OUTPUT_MODEL_NAME = CONFIG.get('output_model_name')

MAX_SEQ_LENGTH = CONFIG.get('max_seq_length')
EPOCHS = CONFIG.get('epochs')
BATCH_SIZE = CONFIG.get('batch_size')
WARMAP_STEPS = CONFIG.get('warmup_steps')
USE_AMP = CONFIG.get('use_amp')

logger.info('All configuration variables loaded successfully')

random.seed(SEED)

# os.environ["PYTORCH_CUDA_ALLOC_CONF"] = f"max_split_size_mb:64"
# Loading distiluse-base-multilingual-cased-v1 model




logger.info('Sentence Transformer model for CL created successfully')
# model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')

sentences = pd.read_csv(DATA_FILE)
logger.info(f'Data file {DATA_FILE} loaded successfully')
# sentences_splitted = [sentence.strip() for text in sentences for sentence in text.split('.') if sentence.strip()]
# sentences_splitted = [s for s in sentences_splitted if len(s.split(' ')) > 3]
train_data = [InputExample(texts=[s, s]) for s in sentences['content']]

train_dataloader = DataLoader(
    train_data, 
    batch_size=BATCH_SIZE, 
    shuffle=True)

logger.info(f'Creating torch dataset completed')



model_names = [
    'sentence-transformers/paraphrase-multilingual-mpnet-base-v2',
    'sentence-transformers/distiluse-base-multilingual-cased-v1',
]

for model_name in model_names:
    word_embedding_model = models.Transformer(model_name, max_seq_length=MAX_SEQ_LENGTH)
    logger.info('Word embedding model created successfully')

    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
    logger.info('Pooling model created successfully')

    train_loss = losses.MultipleNegativesRankingLoss(model)
    logger.info(f'Train loss set properly')

    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    logger.info('Sentence Transformer model for CL created successfully')

    logger.info('CAN CALL model.fit()')
    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=EPOCHS,
        show_progress_bar=True,
        warmup_steps=WARMAP_STEPS,
        use_amp=USE_AMP,
        checkpoint_path='/models',
        checkpoint_save_steps=2525,
    )
logger.info('TRAINING ENDED SUCCESSFULLY :D')

model.save(OUTPUT_MODEL_NAME)
logger.info(f'Fine tuned model {OUTPUT_MODEL_NAME} saved successfully')