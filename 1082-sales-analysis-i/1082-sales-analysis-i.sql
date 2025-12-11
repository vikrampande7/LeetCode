# Write your MySQL query statement below
WITH MaxSales AS (SELECT seller_id, SUM(price) AS TotalSales FROM Sales GROUP BY seller_id ORDER BY SUM(price) DESC)
SELECT seller_id FROM MaxSales WHERE TotalSales = (SELECT MAX(TotalSales) FROM MaxSales)

