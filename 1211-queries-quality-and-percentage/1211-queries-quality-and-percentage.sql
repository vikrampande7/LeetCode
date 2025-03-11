# Write your MySQL query statement below
SELECT 
    a.query_name,
    ROUND(AVG(a.rating / a.position),2) AS quality,
    ROUND((SELECT COUNT(query_name) FROM Queries WHERE rating < 3) / (SELECT COUNT(query_name) FROM Queries) * 100, 2) AS poor_query_percentage 
FROM
    Queries a
WHERE 
    query_name IS NOT NULL
GROUP BY a.query_name

