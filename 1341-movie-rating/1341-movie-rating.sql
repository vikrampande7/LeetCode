# Write your MySQL query statement below
WITH avgMovieRatingFeb AS (
    SELECT 
        movie_id, 
        AVG(rating) AS avgRating
    FROM MovieRating
    WHERE created_at BETWEEN DATE('2020-02-01') AND DATE('2020-02-28')
    GROUP BY movie_id
),

topMovie AS (
    SELECT 
        title AS results
    FROM Movies
    WHERE movie_id IN (
        SELECT movie_id
        FROM avgMovieRatingFeb
        WHERE avgRating = (
            SELECT MAX(avgRating)
            FROM avgMovieRatingFeb
        )
    )
    ORDER BY title
    LIMIT 1
),

movieCount AS (
    SELECT 
        user_id, 
        COUNT(movie_id) AS countMovies
    FROM MovieRating 
    GROUP BY user_id
),

topName AS (
    SELECT 
        name AS results
    FROM Users 
    WHERE user_id IN (
        SELECT user_id 
        FROM movieCount 
        WHERE countMovies = (
            SELECT MAX(countMovies) 
            FROM movieCount
        )
    )
    ORDER BY name
    LIMIT 1
),

Results AS (
    SELECT * FROM topName
    UNION
    SELECT * FROM topMovie
),

Final AS (
    SELECT results,
           ROW_NUMBER() OVER (
               PARTITION BY results 
               ORDER BY (SELECT NULL)
           ) AS RowNum
    FROM Results
)

SELECT results FROM Final WHERE RowNum < 2

