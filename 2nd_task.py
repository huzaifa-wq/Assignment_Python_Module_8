import mysql.connector


connection = mysql.connector.connect(

    port= 3306,
    host='127.0.0.1',
    user="huzaifa",
    password="huzaifa",
    database="flight_game",
    autocommit=True
)



cursor = connection.cursor()

# Ask user for area code
area_code = input("Enter area code (e.g. FI): ").upper()

# SQL query
sql = """
SELECT type, COUNT(*) 
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY type
"""

cursor.execute(sql, (area_code,))
results = cursor.fetchall()

# Print results
if results:
    for row in results:
        print(row[1], row[0])
else:
    print("No airports found for this area code.")

# Close connection
cursor.close()
connection.close()
