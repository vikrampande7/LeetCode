# Write your MySQL query statement below
SELECT d.name AS Department, t.name AS Employee, Salary 
FROM (
  SELECT name, salary, departmentId, 
    DENSE_RANK() OVER (
      PARTITION BY departmentId 
      ORDER BY salary DESC
    ) AS r
  FROM Employee
) AS t
LEFT JOIN Department d ON d.id = t.departmentId
WHERE r < 4;