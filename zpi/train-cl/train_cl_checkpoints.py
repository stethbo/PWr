import os
import random
import logging
import yaml
import pandas as pd

from sentence_transformers import SentenceTransformer, InputExample
from sentence_transformers import models, losses, evaluation
from torch.utils.data import DataLoader

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
CHECKPOINT_SAVE_STEPS = CONFIG.get('checkpoint_save_steps')

logger.info('All configuration variables loaded successfully')

random.seed(SEED)

def clean_up_data(data: pd.DataFrame) -> pd.DataFrame:
    data.dropna(inplace=True)
    return data


def train_model(model_name: str, dir_name: str):
    try:
        sentences = pd.read_csv(DATA_FILE)
    except Exception as e:
        logger.error(f'Error while loading data file {DATA_FILE}: {e}')
        exit(1)

    logger.info(f'Data loaded successfully')

    sentences = clean_up_data(sentences)
    logger.info(f'Data cleaned up successfully')

    train_data = [InputExample(texts=[s, s]) for s in sentences['content']]
    train_dataloader = DataLoader(
        train_data, 
        batch_size=BATCH_SIZE,
        shuffle=True)

    logger.info(f'Creating torch dataset completed')

    word_embedding_model = models.Transformer(model_name, max_seq_length=MAX_SEQ_LENGTH)
    logger.info('Word embedding model created successfully')

    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
    logger.info('Pooling model created successfully')

    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    logger.info('Sentence Transformer model for CL created successfully')
    train_loss = losses.MultipleNegativesRankingLoss(model)
    logger.info(f'Train loss set properly')

    checkpoints_dir = os.path.join(os.getcwd(), dir_name)
    logger.info(f'Checkpoints directory: {checkpoints_dir}')
    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=EPOCHS,
        show_progress_bar=True,
        warmup_steps=WARMAP_STEPS,
        use_amp=USE_AMP,
        checkpoint_path=checkpoints_dir,
        checkpoint_save_steps=CHECKPOINT_SAVE_STEPS,
    )

    logger.info(f'TRAINING OF {model_name} ENDED SUCCESSFULLY :D')
    model.save(OUTPUT_MODEL_NAME + model_name)
    logger.info(f'Fine tuned model {OUTPUT_MODEL_NAME + model_name} saved successfully')

if __name__ == '__main__':
    model_names = {
        'sentence-transformers/paraphrase-multilingual-mpnet-base-v2': 'models/paraphrase-multilingual-mpnet-base-v2',
        'sentence-transformers/distiluse-base-multilingual-cased-v1': 'models/distiluse-base-multilingual-cased-v1',
    }

    for model, dir_name in model_names.items():
        try:
            train_model(model, dir_name)
        except Exception as e:
            logger.error(f'Error while training model {model}: {e}')
