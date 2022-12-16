--Exercise 3 
--Show the most recent five orders that were purchased from account numbers that have spent more than $70,000 with 
--AdventureWorks

Use AdventureWorks2008R2;
GO
ALTER VIEW vWOrderByAccofmorethan70k
AS
SELECT ROW_NUMBER()
 OVER (PARTITION BY SOH.CustomerID ORDER BY OrderDate DESC) OrderRow ,CustomerID, SalesOrderID, OrderDate
FROM Sales.SalesOrderHeader AS SOH
WHERE AccountNumber IN(
						SELECT AccountNumber
						FROM Sales.SalesOrderHeader
						GROUP BY AccountNumber
						HAVING Sum(SubTotal) > 70000
						);
GO
SELECT * FROM vWOrderByAccofmorethan70k
WHERE OrderRow <= 5 
ORDER BY CustomerID, OrderRow;
