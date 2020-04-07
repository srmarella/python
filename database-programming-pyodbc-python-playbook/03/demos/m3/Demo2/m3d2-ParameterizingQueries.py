import pyodbc

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
with pyodbc.connect(connectionString) as connection:
        cursor = connection.cursor()
        #parameterized
        tsqlparam = '''--parameterized
                SELECT TOP 10 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
                FROM Application.Cities cities 
                INNER JOIN Application.StateProvinces sprovs
                ON cities.StateProvinceID=sprovs.StateProvinceID
                WHERE StateProvinceName = ?
                AND cities.LatestRecordedPopulation IS NOT NULL
                ORDER BY cities.LatestRecordedPopulation DESC;'''
        state1 = 'California'
        state2 = 'Texas'
        cursor.execute(tsqlparam,state1)
        cursor.execute(tsqlparam,state2)
        input('Press Enter to continue...')

        #parameterized with input size
        cursor.setinputsizes([(pyodbc.SQL_WVARCHAR, 50, 0)])
        tsqlparamsized = '''--parameterized with type size
                SELECT TOP 10 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
                FROM Application.Cities cities 
                INNER JOIN Application.StateProvinces sprovs
                ON cities.StateProvinceID=sprovs.StateProvinceID
                WHERE StateProvinceName = ?
                AND cities.LatestRecordedPopulation IS NOT NULL
                ORDER BY cities.LatestRecordedPopulation DESC;'''
        state1 = 'California'
        state2 = 'Texas'
        cursor.execute(tsqlparamsized,state1)
        cursor.execute(tsqlparamsized,state2)
        input('Press Enter to continue...')



