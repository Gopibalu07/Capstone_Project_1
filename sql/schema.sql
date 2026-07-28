CREATE TABLE dim_fund(

amfi_code TEXT PRIMARY KEY,

fund_house TEXT,

scheme_name TEXT,

category TEXT,

expense_ratio REAL

);

CREATE TABLE fact_nav(

id INTEGER PRIMARY KEY AUTOINCREMENT,

amfi_code TEXT,

nav_date DATE,

nav REAL,

daily_return REAL
);

CREATE TABLE fact_transactions(

tx_id INTEGER PRIMARY KEY,

investor_id TEXT,

amfi_code TEXT,

transaction_date DATE,

amount REAL,

transaction_type TEXT

);

CREATE TABLE fact_performance(

amfi_code TEXT,

return_1yr REAL,

return_3yr REAL,

return_5yr REAL,

sharpe REAL,

alpha REAL,

beta REAL

);