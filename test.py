import pandas as pd
import pyarrow.parquet as pq

parquet_file = 'utils/test_data.parquet'
table = pq.read_table(parquet_file)
df = table.to_pandas()