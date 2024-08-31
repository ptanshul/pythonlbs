import pyodbc

# Connection details
server = 'mydbss.database.windows.net'
database = 'mydb'
username = 'adminn'
password = 'Azure@123'
driver = '{ODBC Driver 17 for SQL Server}'

# Establish the connection
connection_string = f'DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:mydbss.database.windows.net,1433;Database=mydb;Uid=adminn;Pwd={Azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30';
conn = pyodbc.connect(connection_string)

# Create a cursor object using the connection
cursor = conn.cursor()

# Step 1: Create a simple table
create_table_query = """
IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'TestTable'
)
CREATE TABLE TestTable (
    ID INT PRIMARY KEY,
    Name NVARCHAR(50),
    Age INT
)
"""
cursor.execute(create_table_query)
conn.commit()

# Step 2: Insert data into the table
insert_query = "INSERT INTO TestTable (ID, Name, Age) VALUES (?, ?, ?)"
data = [
    (1, 'Alice', 30),
    (2, 'Bob', 25),
    (3, 'Charlie', 35)
]
cursor.executemany(insert_query, data)
conn.commit()

# Step 3: Retrieve data from the table
select_query = "SELECT * FROM TestTable"
cursor.execute(select_query)

# Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(f'ID: {row.ID}, Name: {row.Name}, Age: {row.Age}')

# Close the connection
cursor.close()
conn.close()
