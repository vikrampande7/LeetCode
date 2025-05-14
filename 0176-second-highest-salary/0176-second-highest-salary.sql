# Write your MySQL query statement below
SELECT DISTINCT
MAX(salary) AS SecondHighestSalary
FROM
(
SELECT 
id, 
salary,
DENSE_RANK () OVER ( ORDER BY salary DESC) AS rank_no
FROM Employee
) AS tmp
WHERE rank_no = 2