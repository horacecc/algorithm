SELECT a.name AS "Employee"
FROM Employee AS a INNER JOIN Employee AS b
ON a.managerId = b.id AND a.salary > b.salary
