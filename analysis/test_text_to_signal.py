import pandas as pd
from analysis.text_to_signal import generate_tfidf
from utils.config import PROCESSED_DATA_PATH

df = pd.read_parquet(PROCESSED_DATA_PATH)

tfidf_matrix, vectorizer = generate_tfidf(df)

print("TF-IDF matrix shape:", tfidf_matrix.shape)
print("Sample features:", vectorizer.get_feature_names_out()[:10])
