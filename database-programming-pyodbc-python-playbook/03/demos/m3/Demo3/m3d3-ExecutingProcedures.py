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
        #stored proc call capture both result sets
        print('SP with multiple result sets:')
        parameters = ('Jon', 10)
        tsql = '{CALL [Website].[SearchForCustomers_InfoAndInvoices] (?,?)}'
        cursor.execute(tsql, parameters)
        rows = cursor.fetchall()

        while rows:
                pf.printResultsInfo(cursor)
                pf.printResults(rows)
                if cursor.nextset():
                        rows=cursor.fetchall()
                else:
                        rows = None
        
        input('Press Enter to continue...')

        #capturing output parameter
        print('SP with output parameter')
        parameters = ('Jon', 10)
        tsql = '''DECLARE @out int;
                EXEC [Website].[SearchForCustomers_InfoAndInvoices] ?, ?, @out OUTPUT;
                SELECT @out AS outputparameter;'''
        cursor.execute(tsql, parameters)
        
        cursor.nextset()
        cursor.nextset()
        rows = cursor.fetchall()
        pf.printResultsInfo(cursor)
        pf.printResults(rows)
               
        input('Press Enter to continue...')

        #capturing output parameter and return value
        print('SP with output parameter and return value')
        parameters = ('Jon', 10)
        tsql = '''DECLARE @out int;
                DECLARE @return int;
                EXEC @return =  [Website].[SearchForCustomers_InfoAndInvoices] ?, ?, @out OUTPUT;
                SELECT @out AS outputparameter;
                SELECT @return AS returnvalue;'''
        cursor.execute(tsql, parameters)
        
        cursor.nextset()
        cursor.nextset()
        cursor.nextset()
        rows = cursor.fetchall()
        pf.printResultsInfo(cursor)
        pf.printResults(rows)
        input('Press Enter to continue...')

