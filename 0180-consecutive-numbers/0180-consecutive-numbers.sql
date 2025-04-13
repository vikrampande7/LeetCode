# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM
    (
    SELECT
        *,
        LEAD(num) OVER(ORDER BY id) AS next_num,
        LAG(num) OVER(ORDER BY id) AS prev_num
    FROM 
        Logs
    ) AS tmp
WHERE 
    num = prev_num AND num = next_num