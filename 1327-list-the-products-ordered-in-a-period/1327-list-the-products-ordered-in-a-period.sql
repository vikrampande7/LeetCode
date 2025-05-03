# Write your MySQL query statement below
SELECT
    p.product_name,
    SUM(o.unit) AS unit
FROM 
    Products p
JOIN
    Orders o
ON p.product_id = o.product_id
WHERE order_date > DATE('2020-01-31') AND order_date < DATE('2020-03-01')
GROUP BY 1
HAVING SUM(o.unit) >= 100
