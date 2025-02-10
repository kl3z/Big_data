import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
df = pd.read_csv("C:\\Users\\garci\\OneDrive\\Área de Trabalho\\Ambiente de trabalho unbunto\\Cienciadedados\\IPL\\BigData\\Trabalho\\synthetic_fraud_data.csv", sep=";")
table = pa.Table.from_pandas(df)
pq.write_table(table, 'C:\\Users\\garci\\OneDrive\\Área de Trabalho\\Ambiente de trabalho unbunto\\Cienciadedados\\IPL\\BigData\\Trabalho\\transactions.parquet')