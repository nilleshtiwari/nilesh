--Exercise 5

--Write a Procedure supplying name information from the Person.Person table and accepting a filter for the first name. Alter the above 
--Store Procedure to supply Default Values if user does not enter any value. ( Use AdventureWorks)

Use AdventureWorks2008R2;
GO

CREATE PROCEDURE PersonInfo
@FirstName varchar(50)
AS
SELECT FirstName,MiddleName,LastName
FROM Person.Person
WHERE FirstName=@FirstName;
GO

exec dbo.PersonInfo 'Ken'

ALTER PROCEDURE PersonInfo
@FirstName varchar(50) = 'Ken'
AS
SELECT FirstName,MiddleName,LastName
FROM Person.Person
WHERE FirstName=@FirstName;

-- default value given is Ken as the first name
exec dbo.PersonInfo
exec dbo.PersonInfo 'Roberto'
