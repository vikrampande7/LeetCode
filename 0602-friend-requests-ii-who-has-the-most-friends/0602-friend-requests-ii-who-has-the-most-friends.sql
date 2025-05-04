# Write your MySQL query statement below
WITH reqSent AS (
SELECT
    accepter_id,
    COUNT(requester_id) AS friends
FROM
    RequestAccepted
GROUP BY accepter_id ),

reqAccepted AS (
SELECT
    requester_id,
    COUNT(accepter_id) AS friends
FROM
    RequestAccepted
GROUP BY requester_id
)

SELECT
    a.requester_id AS id,
    IFNULL(s.friends, 0) + IFNULL(a.friends,0) AS num
FROM reqAccepted a
LEFT JOIN reqSent s
ON a.requester_id = s.accepter_id
ORDER BY 2 DESC
LIMIT 1

