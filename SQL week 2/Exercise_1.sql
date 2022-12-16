-- Exercise - 1

-- Q.1 Display the number of records in the [SalesPerson] table. (Schema(s) involved: Sales)
SELECT COUNT(*) AS TotalFields FROM Sales.SalesPerson



-- Q.2 Select both the FirstName and LastName of records from the Person table where the FirstName begins with the letter ‘B’. 

SELECT FirstName+ ' ' +  LastName AS FullName FROM Person.Person WHERE Person.FirstName Like 'B%';



-- Q.3 Select a list of FirstName and LastName for employees where Title is one of Design Engineer, Tool Designer or Marketing

SELECT FirstName,LastName,JobTitle 
FROM Person.Person 
INNER JOIN HumanResources.Employee
ON Person.Person.BusinessEntityID=HumanResources.Employee.BusinessEntityID
AND  JobTitle LIKE '%Design Engineer%' OR JobTitle LIKE '%Tool Designer %' OR JobTitle LIKE'%Marketing Assistant%'



-- Q.4 Display the Name and Color of the Product with the maximum weight. 

SELECT Product.Name, Product.Color
FROM Production.Product 
WHERE Product.Weight = (
					SELECT MAX(Product.Weight) from Production.Product
					) --USING SUBQUERIES


--Q.5 Display Description and MaxQty fields from the SpecialOffer table. Some of the MaxQty values are NULL, in this case display 
--the value 0.00 instead.

SELECT Sales.SpecialOffer.Description, ISNULL(Sales.SpecialOffer.MaxQty, 0.00) AS MaxQty FROM Sales.SpecialOffer



--Q.6 display the overall Average of the [CurrencyRate].[AverageRate] values for the exchange rate ‘USD’ to ‘GBP’ for the year 2005 
--i.e. FromCurrencyCode = ‘USD’ and ToCurrencyCode = ‘GBP’.

SELECT AVG(CurrencyRate.AverageRate) 
FROM Sales.CurrencyRate
WHERE YEAR(CurrencyRate.CurrencyRateDate) = 2005 
and CurrencyRate.FromCurrencyCode = 'USD' 
and CurrencyRate.ToCurrencyCode = 'GBP';



--Q.7  Display the FirstName and LastName of records from the Person table where FirstName contains the letters ‘ss’. Display an 
--additional column with sequential numbers for each row returned beginning at integer 1

SELECT ROW_NUMBER() OVER(ORDER BY FirstName asc ) AS RowNumber, FirstName, LastName
FROM Person.Person
WHERE FirstName LIKE '%ss%';



--Q.8 Sales people receive various commission rates that belong to 1 of 4 bands.

SELECT BusinessEntityID AS SalesPersonID, 'Commision Band' = 
CASE 
	WHEN CommissionPct = 0 THEN 'Band 0'
	WHEN CommissionPct > 0 AND  CommissionPct <= 1 THEN 'Band 1'
	WHEN CommissionPct > 1 AND  CommissionPct <= 1.5 THEN 'Band 2'
	WHEN CommissionPct > 1.5 THEN 'Band 3'
END
FROM sales.SalesPerson;



--Q.9 Display the managerial hierarchy from Ruth Ellerbrock (person type – EM) up to CEO Ken Sanchez.

DECLARE @id INT;
SELECT @id = BusinessEntityID
FROM Person.Person
WHERE FirstName='Ruth' and LastName ='Ellerbrock' and PersonType='EM'
EXEC dbo.uspGetEmployeeManagers @BusinessEntityID=@ID;



--Q.10 Display the ProductId of the product with the largest stock level. Hint: Use the Scalar-valued function [dbo].

SELECT Max(dbo.ufnGetStock(ProductID)) AS [ProductID with largest Stock level] FROM Production.Product;


