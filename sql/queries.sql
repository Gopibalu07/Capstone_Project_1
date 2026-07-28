SELECT *
FROM dim_fund
LIMIT 5;

SELECT
amfi_code,
AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

SELECT
amfi_code,
AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;