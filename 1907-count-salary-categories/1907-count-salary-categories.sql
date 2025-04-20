# Write your MySQL query statement below
WITH categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
),

segments AS (
SELECT 
    account_id,
    income,
    CASE 
        WHEN income < 20000 THEN 'Low Salary'   
        WHEN income >= 20000  AND income <= 50000 THEN 'Average Salary'
        WHEN income > 50000 THEN 'High Salary'  
    END AS category
FROM
    Accounts
)

SELECT c.category, COUNT(s.account_id) AS accounts_count 
FROM categories c
LEFT JOIN segments s
ON c.category = s.category
GROUP BY c.category
ORDER BY 2 DESC