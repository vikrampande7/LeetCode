# Write your MySQL query statement below
SELECT
    e.employee_id,
    e.name,
    t.reports_count, 
    ROUND(t.average_age) AS average_age
FROM
    Employees e
JOIN
(
SELECT
    reports_to,
    COUNT(employee_id) AS reports_count,
    AVG(age) AS average_age
FROM 
    Employees
WHERE 
    reports_to IS NOT NULL
GROUP BY
    reports_to
) t
ON 
    e.employee_id = t.reports_to
ORDER BY 1

