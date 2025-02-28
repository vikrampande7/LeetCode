# Write your MySQL query statement below
-- SELECT 
--     machine_id,
--     ROUND(AVG(time_req),3) AS processing_time
-- FROM
-- (
-- SELECT
--     machine_id,
--     process_id,
--     MAX(timestamp) - MIN(timestamp) AS time_req
-- FROM
--     Activity
-- GROUP By
--     process_id, machine_id
-- ) AS temp
-- GROUP BY machine_id

SELECT 
    s.machine_id, 
    ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
FROM Activity s
JOIN Activity e 
    ON s.machine_id = e.machine_id 
    AND s.process_id = e.process_id
    AND s.activity_type = 'start' 
    AND e.activity_type = 'end'
GROUP BY s.machine_id;


