--Exercise - 2
--Write separate queries using a join, a subquery, a CTE, and then an EXISTS to list all AdventureWorks customers who have not placed 
--an order.
USE AdventureWorks2008R2;
GO

-- Using Join
SELECT *
FROM Sales.Customer C
LEFT OUTER JOIN Sales.SalesOrderHeader SOH ON C.CustomerID = SOH.CustomerID
WHERE SOH.SalesOrderID IS NULL
ORDER BY C.CustomerID



--Using CTE:
WITH CustomerWithOutOrder AS
(   SELECT customerID, SalesOrderID
    FROM Sales.SalesOrderHeader 
)
SELECT *
FROM Sales.Customer C
LEFT OUTER JOIN CustomerWithOutOrder CWO ON C.customerID = CWO.customerID
WHERE CWO.SalesOrderID IS NULL
ORDER BY C.CustomerID



--Using SubQuery:
SELECT *
FROM Sales.Customer C
WHERE C.CustomerID NOT  IN (
						SELECT SOH.CustomerID
						FROM Sales.SalesOrderHeader SOH
						WHERE SOH.SalesOrderID IS NOT NULL
					  );

SELECT * FROM Sales.SalesOrderHeader WHERE SalesOrderHeader.CustomerID = 46					


--Using EXISTS:
SELECT *
FROM Sales.Customer C
where NOT EXISTS(
			SELECT *
			FROM Sales.SalesOrderHeader SOH
			WHERE SOH.SalesOrderID IS NOT NULL
			AND C.customerID = SOH.customerID
			)
ORDER BY C.CustomerID
