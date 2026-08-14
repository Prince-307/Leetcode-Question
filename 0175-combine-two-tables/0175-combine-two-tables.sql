# Write your MySQL query statement below
SELECT firstname,lastname,city,state
FROM Person AS p
LEFT JOIN Address as a
ON p.personId = a.personId