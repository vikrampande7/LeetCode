# Write your MySQL query statement below
WITH CTE AS
(SELECT
    player_id,
    min(event_date) AS first_date,
    DATE_ADD(MIN(event_date), INTERVAL 1 DAY) AS next_day
FROM 
    Activity
GROUP BY player_id)

SELECT 
ROUND(
    (SELECT COUNT(DISTINCT player_id) FROM Activity
    WHERE (player_id, event_date) IN (SELECT player_id, next_day FROM cte)) 
    / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction