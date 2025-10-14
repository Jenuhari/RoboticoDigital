CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    WITH cte AS
     (SELECT * , DENSE_RANK() OVER(ORDER BY Salary DESC) AS rnk
     FROM Employee)
     SELECT DISTINCT IFNULL(Salary, null)
     FROM cte
     WHERE rnk = N

  );
END