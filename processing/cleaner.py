import pandas as pd
import regex as re
from utils.logger import setup_logger

logger = setup_logger()


def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Keep emojis & Indian language unicode
    text = re.sub(r"[^\p{L}\p{N}\p{P}\p{S}\s]", "", text)

    return text.lower()


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting data cleaning")

    df = df.dropna(subset=["content"])
    df["clean_text"] = df["content"].apply(normalize_text)

    # Remove very short tweets
    df = df[df["clean_text"].str.len() > 10]

    logger.info(f"Cleaned dataset size: {len(df)}")
    return df
