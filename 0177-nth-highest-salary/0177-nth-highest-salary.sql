CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT salary
      FROM (
        SELECT salary,
        DENSE_RANK() OVER (ORDER BY salary desc)
        AS rnk FROM EMPLOYEE
      ) AS ranked
      where rnk=N
      LIMIT 1
  );
END