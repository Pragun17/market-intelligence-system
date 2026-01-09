import pandas as pd
from analysis.text_to_signal import generate_tfidf
from analysis.aggregation import build_signal
from analysis.visualize import plot_signal_distribution
from utils.config import PROCESSED_DATA_PATH

df = pd.read_parquet(PROCESSED_DATA_PATH)

tfidf_matrix, vectorizer = generate_tfidf(df)

# Rebuild raw signal for visualization
import numpy as np

feature_names = vectorizer.get_feature_names_out()
weights = np.zeros(len(feature_names))

for i, term in enumerate(feature_names):
    if term in ["bullish", "breakout", "buy", "rally"]:
        weights[i] = 1
    elif term in ["bearish", "sell", "crash"]:
        weights[i] = -1

raw_signal = tfidf_matrix.dot(weights)

plot_signal_distribution(raw_signal)