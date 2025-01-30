import mysql.connector
def connectindb():
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='shanmukreddy'
    )
    return connection
