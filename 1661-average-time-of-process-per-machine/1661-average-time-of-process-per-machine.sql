# Write your MySQL query statement below
SELECT 
    machine_id,
    ROUND(AVG(time_req),3) AS processing_time
FROM
(
SELECT
    machine_id,
    process_id,
    MAX(timestamp) - MIN(timestamp) AS time_req
FROM
    Activity
GROUP By
    process_id, machine_id
) AS temp
GROUP BY machine_id


