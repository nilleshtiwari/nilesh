--Exercise 4
--Create a function that takes as inputs a SalesOrderID, a Currency Code, and a date, and returns a table of all the SalesOrderDetail rows 
--for that Sales Order including Quantity, ProductID, UnitPrice, and the unit price converted to the target currency based on the end of 
--day rate for the date provided. Exchange rates can be found in the Sales.CurrencyRate table. (Use AdventureWorks)

Use AdventureWorks2008R2;
GO
CREATE FUNCTION SaleOrderDetail (
 @SalesOrderID INT,
 @TargetCurrencyCode nchar(3),
 @CurrencyRateDate DATETIME
)
RETURNS @Table TABLE (
 SalesOrderDetailID INT,
 OrderQty INT,
 ProductID INT,
 UnitPrice MONEY,
 UnitPriceConverted MONEY
)
AS
BEGIN
 DECLARE @EndOfDayRate MONEY;

 SELECT @EndOfDayRate = EndOfDayRate
 FROM Sales.CurrencyRate
 WHERE CurrencyRateDate = @CurrencyRateDate
 AND ToCurrencyCode = @TargetCurrencyCode;
 INSERT @Table
 SELECT SalesOrderDetailID,
 OrderQty,
 ProductID,
 UnitPrice,
 UnitPrice * @EndOfDayRate
 FROM Sales.SalesOrderDetail
 WHERE SalesOrderID = @SalesOrderID
 RETURN;
END
GO


SELECT *
FROM SaleOrderDetail(43659,'EUR','2005-07-05 00:00:00.000');


