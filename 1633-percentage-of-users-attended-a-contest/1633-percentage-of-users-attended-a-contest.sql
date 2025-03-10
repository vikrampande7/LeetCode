# Write your MySQL query statement below
SELECT 
    r.contest_id,
    ROUND((COUNT(u.user_id) / (SELECT COUNT(user_id) FROM Users))*100,2) AS percentage 
FROM
    Users u
JOIN
    Register r
ON 
    u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY 2 DESC, 1 ASC
