import pyodbc
import sys
sys.path.append(sys.path[0]+'/../..')
import printFunctions as pf

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
with pyodbc.connect(connectionString) as connection:
        cursor = connection.cursor()
        #stored proc call to pass a table variable
        print('SP with table variable parameter:')
        items = []
        items.insert(0,(1,1,'first item',1))
        items.insert(0,(1,2,'second item',1))

        #create an equivalent temp table
        tsql = '''IF OBJECT_ID('tempdb..#TempOrderLines') IS NOT NULL
	        DROP TABLE #TempOrderLines;
                CREATE TABLE #TempOrderLines (
                [OrderReference] [int] NULL,
	        [StockItemID] [int] NULL,
	        [Description] [nvarchar](100) COLLATE Latin1_General_100_CI_AS NULL,
	        [Quantity] [int] NULL)'''
        
        cursor.execute(tsql)

        #now insert all the records into the temp table
        cursor.fast_executemany = True
        cursor.executemany('''INSERT INTO #TempOrderLines([OrderReference], [StockItemID],[Description],[Quantity]) 
                                values (?, ?, ?, ?)''', items)
        
        #now move the records and call the SP
        tsql='''SET NOCOUNT ON;
                DECLARE @OrderLines [Website].[OrderLineList];
                INSERT INTO @OrderLines SELECT * FROM #TempOrderLines;
                EXEC [Website].[GetItemNameAndRetailPrice] @OrderLines;'''
        cursor.execute(tsql)
        rows = cursor.fetchall()

        while rows:
                pf.printResultsInfo(cursor)
                pf.printResults(rows)
                if cursor.nextset():
                        rows=cursor.fetchall()
                else:
                        rows = None
        
        input('Press Enter to continue...')

