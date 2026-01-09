import pandas as pd
from analysis.text_to_signal import generate_tfidf
from analysis.aggregation import build_signal
from utils.config import PROCESSED_DATA_PATH

df = pd.read_parquet(PROCESSED_DATA_PATH)

tfidf_matrix, vectorizer = generate_tfidf(df)

signal = build_signal(
    tfidf_matrix,
    vectorizer.get_feature_names_out()
)

print(signal)
