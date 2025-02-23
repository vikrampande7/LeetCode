# Write your MySQL query statement below
-- SELECT DISTINCT
-- a.author_id AS id
-- FROM Views a
-- INNER JOIN Views b on a.author_id = b.author_id
-- AND a.author_id = b.viewer_id
-- ORDER BY a.author_id

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id