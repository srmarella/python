import pyodbc

def printResults(rows):
        if len(rows)==0:
                print('No rows returned')
        else:
                print(str(len(rows)) + ' row(s) returned:')        
                print(', '.join(c[0] for c in rows[0].cursor_description))
                for row in rows:
                        print(', '.join(str(value) for value in row))

def printResultsInfo(cursor):
        print('Result description:')
        for column in cursor.description:
                print('Name: ' + column[0])
                print('Python type: ' + str(column[1]))
                print('Nullable: ' + str(column[6]))