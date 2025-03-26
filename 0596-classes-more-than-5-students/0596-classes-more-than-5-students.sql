# Write your MySQL query statement below
-- SELECT
--     class
-- FROM
--     Courses
-- GROUP BY 
--     class
-- HAVING COUNT(DISTINCT student) > 5
SELECT class FROM
(
SELECT
    class,
    COUNT(DISTINCT student) AS StudentCount
FROM 
    Courses
GROUP BY 
    class
) temp
WHERE StudentCount >= 5