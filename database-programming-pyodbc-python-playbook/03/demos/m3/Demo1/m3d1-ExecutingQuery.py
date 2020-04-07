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
        #simple query
        tsql = '''SELECT TOP 10 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
                FROM Application.Cities cities 
                INNER JOIN Application.StateProvinces sprovs 
                ON cities.StateProvinceID=sprovs.StateProvinceID
                WHERE StateProvinceName = 'California'
                AND cities.LatestRecordedPopulation IS NOT NULL
                ORDER BY cities.LatestRecordedPopulation DESC;'''
        cursor.execute(tsql)
        rows = cursor.fetchall()

        #note the -1 return for a SELECT
        print('Cursor row count: ' + str(cursor.rowcount))

        #print results
        pf.printResultsInfo(cursor)
        pf.printResults(rows)
        input('Press Enter to continue...')

