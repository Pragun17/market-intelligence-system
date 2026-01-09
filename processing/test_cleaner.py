import pandas as pd
from processing.cleaner import clean_dataframe
from utils.config import RAW_DATA_PATH

df = pd.read_parquet(RAW_DATA_PATH)
clean_df = clean_dataframe(df)

print(clean_df[["content", "clean_text"]].head())
