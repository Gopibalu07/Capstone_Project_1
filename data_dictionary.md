# Bluestock Mutual Fund Analytics Platform

## Data Dictionary
## 1. fund_master
| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | Mutual Fund Company Name |
| scheme_name | TEXT | Complete Scheme Name |
| category | TEXT | Equity, Debt or Hybrid |
| sub_category | TEXT | Large Cap, Mid Cap etc. |
| expense_ratio_pct | REAL | Expense ratio (%) |
| risk_category | TEXT | Low, Moderate, High |


## 2. nav_history

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | TEXT | Fund Identifier |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |


## 3. investor_transactions

| Column | Type | Description |
|---------|------|-------------|
| investor_id | TEXT | Unique Investor ID |
| transaction_date | DATE | Transaction Date |
| amfi_code | TEXT | Fund Code |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | INTEGER | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | T30 or B30 |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Male/Female |
| annual_income_lakh | REAL | Annual Income |
| payment_mode | TEXT | UPI, Net Banking, etc. |
| kyc_status | TEXT | Verified or Pending |


## 4. scheme_performance

| Column | Type | Description |
|---------|------|-------------|
| return_1yr_pct | REAL | 1 Year Return |
| return_3yr_pct | REAL | 3 Year CAGR |
| return_5yr_pct | REAL | 5 Year CAGR |
| benchmark_3yr_pct | REAL | Benchmark Return |
| alpha | REAL | Excess Return |
| beta | REAL | Market Sensitivity |
| sharpe_ratio | REAL | Risk Adjusted Return |
| sortino_ratio | REAL | Downside Risk Metric |
| std_dev_ann_pct | REAL | Annual Standard Deviation |
| max_drawdown_pct | REAL | Worst Decline |


## Data Sources

| Dataset | Source |
|---------|--------|
| fund_master | AMFI India |
| nav_history | mfapi.in |
| aum_by_fund_house | AMFI Quarterly Reports |
| monthly_sip_inflows | AMFI Monthly Notes |
| investor_transactions | Simulated Bluestock Dataset |


