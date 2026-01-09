import pandas as pd
from processing.cleaner import clean_dataframe
from processing.deduplicator import deduplicate
from utils.config import RAW_DATA_PATH

df = pd.read_parquet(RAW_DATA_PATH)

clean_df = clean_dataframe(df)
dedup_df = deduplicate(clean_df)

print(f"Before: {len(clean_df)}")
print(f"After: {len(dedup_df)}")
