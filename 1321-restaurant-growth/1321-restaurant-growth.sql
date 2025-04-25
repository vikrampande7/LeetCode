# Write your MySQL query statement below  
WITH rollingAmount AS (
SELECT
    visited_on,
    SUM(amount) OVER (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount
FROM Customer 
)

SELECT DISTINCT
    visited_on,
    amount,
    ROUND((amount/7),2) AS average_amount
FROM 
    rollingAmount
WHERE 
    DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6

