# Write your MySQL query statement below
-- SELECT v.customer_id, COUNT(t.transaction_id) AS count_no_trans
-- FROM
-- Visits v
-- LEFT JOIN
-- Transactions t
-- ON v.visit_id = t.visit_id
-- WHERE t.amount = 0
-- GROUP BY v.customer_id

-- SELECT COUNT(*) FROM Visits WHERE visit_id IS NULL 

SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM
Visits v 
LEFT JOIN
Transactions t 
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id
