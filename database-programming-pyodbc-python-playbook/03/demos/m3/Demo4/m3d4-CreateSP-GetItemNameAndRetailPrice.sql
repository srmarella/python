USE [WideWorldImporters]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE OR ALTER PROCEDURE [Website].[GetItemNameAndRetailPrice]
@OrderLines Website.OrderLineList READONLY
WITH EXECUTE AS OWNER
AS
BEGIN
    SELECT ols.Description,si.StockItemName,si.RecommendedRetailPrice 
	FROM [Warehouse].StockItems si
	INNER JOIN @OrderLines ols 
	ON si.StockItemID = ols.StockItemID
END;
GO


