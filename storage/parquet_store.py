import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from utils.logger import setup_logger

logger = setup_logger()


def save_parquet(data, path):
    os.makedirs(path.parent, exist_ok=True)

    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df, preserve_index=False)

    pq.write_table(table, str(path))
    logger.info(f"Saved {len(df)} records to {path}")
