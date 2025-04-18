# Write your MySQL query statement below
WITH weight_sums AS (
    SELECT 
        person_id,
        person_name,
        weight,
        turn,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue 
)

SELECT
    person_name
FROM
(
SELECT 
    person_id,
    person_name,
    weight,
    turn,
    COALESCE(
        LAG(cumulative_weight) OVER (ORDER BY turn),
        weight
    ) AS sum_previous_weights
FROM weight_sums
) AS tmp
WHERE sum_previous_weights < 1000
ORDER BY sum_previous_weights DESC
LIMIT 1

