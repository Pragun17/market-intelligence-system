import hashlib
import pandas as pd
from utils.logger import setup_logger

logger = setup_logger()


def text_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def deduplicate(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting deduplication")

    df["text_hash"] = df["clean_text"].apply(text_hash)

    before = len(df)
    df = df.drop_duplicates(subset=["text_hash"])
    after = len(df)

    logger.info(f"Removed {before - after} duplicate tweets")
    return df
