# Write your MySQL query statement below
WITH 

cte1 AS (    
SELECT product_id, MAX(change_date) AS maxChangeDate FROM Products WHERE change_date < DATE('2019-08-17') GROUP BY product_id 
),

cte2 AS (  
SELECT p.product_id, new_price AS price FROM Products p LEFT JOIN cte1 ON p.product_id = cte1.product_id WHERE p.change_date = cte1.maxChangeDate),

cte3 AS (SELECT product_id, 10 as price FROM Products WHERE change_date > DATE('2019-08-17'))

SELECT * FROM cte2 
UNION
SELECT * FROM cte3 
ORDER BY product_id

