-- # Write your MySQL query statement below
-- SELECT
--     c.customer_id
-- FROM
--     Customer c 
-- JOIN 
--     Product p
-- ON c.product_key = p.product_key
-- WHERE
--     c.product_key IN (SELECT DISTINCT product_key FROM Product)
-- GROUP BY c.customer_id
-- HAVING COUNT(c.customer_id) = (SELECT COUNT(DISTINCT product_key) FROM Product)

SELECT 
    c.customer_id
FROM 
    Customer c
GROUP BY 
    1
HAVING COUNT(DISTINCT c.product_key) = (SELECT COUNT(*) FROM Product)
