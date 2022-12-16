--Exercise 6
--Write a trigger for the Product table to ensure the list price can never be raised more than 15 Percent in a single change. 
--modi fy the above trigger to execute its check code only if the ListPrice column is updated (Use AdventureWorks Database).
USE AdventureWorks2008R2;
GO
CREATE TRIGGER CheckPrice
ON Production.Product
INSTEAD OF UPDATE
AS
BEGIN
IF EXISTS(
			SELECT *
			FROM inserted i
			JOIN deleted d
			ON i.ProductID = d.ProductID
			WHERE i.ListPrice > (d.ListPrice * 1.15)
		  )
	BEGIN 
		RAISERROR('Price increased may not be greater than 15 percent.Therefore Transaction Failed.',16,1)
		ROLLBACK TRAN
	END
END
GO


ALTER TRIGGER CheckPrice
ON Production.Product
FOR UPDATE
AS
IF UPDATE(ListPrice)
BEGIN
IF EXISTS(
			SELECT *
			FROM inserted i
			JOIN deleted d
			ON i.ProductID = d.ProductID
			WHERE i.ListPrice > (d.ListPrice * 1.15)
		  )
	BEGIN 
		RAISERROR('Price increased may not be greater than 15 percent.Therefore Transaction Failed.',16,1)
		ROLLBACK TRAN
	END
END
GO
--test quey
UPDATE Production.Product
SET ListPrice = 500
WHERE ProductID = 745

--check changes
select ProductID, Name, ListPrice from Production.Product
where ProductID=745