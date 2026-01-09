import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.logger import setup_logger

logger = setup_logger()


def generate_tfidf(df: pd.DataFrame, max_features=1000):
    logger.info("Generating TF-IDF vectors")

    vectorizer = TfidfVectorizer(
        max_features=max_features,
        ngram_range=(1, 2),
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(df["clean_text"])

    logger.info(
        f"TF-IDF shape: {tfidf_matrix.shape} "
        f"(rows=tweets, cols=features)"
    )

    return tfidf_matrix, vectorizer
