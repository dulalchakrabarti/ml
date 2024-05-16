import polars as pl
from datetime import datetime

df = pl.DataFrame(
    {
        "integer": [1, 2, 3],
        "date": [
            datetime(2025, 1, 1),
            datetime(2025, 1, 2),
            datetime(2025, 1, 3),
        ],
        "float": [4.0, 5.0, 6.0],
        "string": ["a", "b", "c"],
    }
)
df.write_csv("output.csv")
df_csv = pl.read_csv("output.csv")
#print(df_csv)
#df.select(pl.col("*"))
#df1 = df.select(pl.col("date", "string"))
df1 = df.filter(
    pl.col("date").is_between(datetime(2025, 1, 2), datetime(2025, 1, 3)),
)

print(df1)

