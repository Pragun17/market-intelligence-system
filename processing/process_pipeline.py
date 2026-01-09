import pandas as pd
from processing.cleaner import clean_dataframe
from processing.deduplicator import deduplicate
from storage.parquet_store import save_parquet
from utils.config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from utils.logger import setup_logger

logger = setup_logger()


def run_processing_pipeline():
    logger.info("Loading raw data")
    df = pd.read_parquet(RAW_DATA_PATH)

    df = clean_dataframe(df)
    df = deduplicate(df)

    save_parquet(df.to_dict(orient="records"), PROCESSED_DATA_PATH)
    logger.info("Processing pipeline completed")


if __name__ == "__main__":
    run_processing_pipeline()
