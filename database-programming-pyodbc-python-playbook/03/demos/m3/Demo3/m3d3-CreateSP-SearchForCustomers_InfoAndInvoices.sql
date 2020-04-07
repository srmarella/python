USE [WideWorldImporters]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE OR ALTER PROCEDURE [Website].[SearchForCustomers_InfoAndInvoices]
@SearchText nvarchar(1000),
@MaximumRowsToReturn int,
@CustomersFound int = 0 OUTPUT
WITH EXECUTE AS OWNER
AS
BEGIN
DECLARE @TotalRowsFound int;

    SELECT TOP(@MaximumRowsToReturn)
           c.CustomerID,
           c.CustomerName,
           ct.CityName,
           c.PhoneNumber,
           c.FaxNumber,
           p.FullName AS PrimaryContactFullName,
           p.PreferredName AS PrimaryContactPreferredName
    FROM Sales.Customers AS c
    INNER JOIN [Application].Cities AS ct
    ON c.DeliveryCityID = ct.CityID
    LEFT OUTER JOIN [Application].People AS p
    ON c.PrimaryContactPersonID = p.PersonID
    WHERE CONCAT(c.CustomerName, N' ', p.FullName, N' ', p.PreferredName) LIKE N'%' + @SearchText + N'%'
    ORDER BY c.CustomerName

	SET @TotalRowsFound = @@ROWCOUNT;
	SET @CustomersFound = @TotalRowsFound;

	SELECT TOP(@MaximumRowsToReturn)
           c.CustomerID,
           c.CustomerName,
           inv.InvoiceID,
		   inv.InvoiceDate,
		   inv.DeliveryInstructions
    FROM Sales.Customers AS c
    INNER JOIN [Sales].Invoices AS inv
    ON c.CustomerID = inv.CustomerID
    LEFT OUTER JOIN [Application].People AS p
    ON c.PrimaryContactPersonID = p.PersonID
    WHERE CONCAT(c.CustomerName, N' ', p.FullName, N' ', p.PreferredName) LIKE N'%' + @SearchText + N'%'
    ORDER BY c.CustomerName

	SET @TotalRowsFound = @TotalRowsFound + @@ROWCOUNT;
	RETURN @TotalRowsFound;

END;

GO


