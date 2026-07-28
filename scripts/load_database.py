from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)

pd.read_csv(
    "data/processed/clean_nav.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/clean_transactions.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/clean_performance.csv"
).to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/raw/01_fund_master.csv"
).to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)