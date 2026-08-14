# Write your MySQL query statement below
SELECT email
FROM (
    SELECT email , COUNT(*)
    FROM Person
    GROUP BY email 
    HAVING COUNT(*) > 1
) AS Email