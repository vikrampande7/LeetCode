-- # Write your MySQL query statement below
-- SELECT
--     ROUND(SUM(CASE WHEN status = 'immediate' THEN 1 END) / COUNT(status),2) * 100 AS immediate_percentage 
-- FROM
-- (
-- SELECT
--     d1.delivery_id,
--     d1.customer_id,
--     d1.order_date,
--     d1.customer_pref_delivery_date ,
--     CASE WHEN d1.order_date = d2.customer_pref_delivery_date THEN 'immediate' ELSE 'scheduled' END AS status
-- FROM
--     Delivery d1
-- JOIN
--     Delivery d2
-- ON
--     d1.delivery_id = d2.delivery_id
-- ) AS tmp

WITH first_orders AS (
    SELECT customer_id, MIN(order_date) AS min_order_date
    FROM Delivery
    GROUP BY customer_id
)
SELECT 
    ROUND(
        SUM(IF(d.customer_pref_delivery_date = fo.min_order_date, 1, 0)) 
        / COUNT(DISTINCT fo.customer_id) * 100, 2
    ) AS immediate_percentage 
FROM first_orders fo
JOIN Delivery d
ON fo.customer_id = d.customer_id  
AND fo.min_order_date = d.order_date;