import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

# prints all
query = 'SELECT * FROM user_data'
cursor.execute(query)
print("\nAll the data")
output = cursor.fetchall()
for row in output:
    print(row)


# prints many (2 rows in this case)
query = 'SELECT * FROM user_data'
cursor.execute(query)
print("\nLimited data")
output = cursor.fetchmany(2)
for row in output:
    print(row)


# prints one row
query = 'SELECT * FROM user_data'
cursor.execute(query)
print("\nOnly one data")
output = cursor.fetchone()
print(output)


# prints all
query = 'SELECT * FROM user_data where user_name = ?'
cursor.execute(query, ('ssioepo',))
print("\nSpecific data")
output = cursor.fetchall()
print(output)



connection.close()
