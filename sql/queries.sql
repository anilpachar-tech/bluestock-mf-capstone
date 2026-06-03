-- 1. Top 5 Fund Houses by AUM

SELECT
    fund_house,
    MAX(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;


-- 2. Average NAV by Scheme


SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;


-- 3. Monthly Average NAV


SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 4. Total Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds With Expense Ratio Less Than 1%


SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Average Investment Amount by Transaction Type


SELECT
    transaction_type,
    ROUND(AVG(amount_inr),2) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 7. Top 10 Schemes by 5-Year Return


SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 8. Highest Sharpe Ratio Funds


SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- 9. Transaction Count by Gender


SELECT
    gender,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY gender;


-- 10. Average Annual Income by City Tier


SELECT
    city_tier,
    ROUND(AVG(annual_income_lakh),2) AS avg_income
FROM fact_transactions
GROUP BY city_tier
ORDER BY avg_income DESC;