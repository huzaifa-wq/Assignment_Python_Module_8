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

# Ask user for ICAO code
icao = input("Enter ICAO code: ").upper()

# SQL query
sql = """
SELECT name, municipality
FROM airport
WHERE ident = %s
"""

cursor.execute(sql, (icao,))
result = cursor.fetchone()

# Print result
if result:
    print("Airport name:", result[0])
    print("Location (town):", result[1])
else:
    print("No airport found with this ICAO code.")

# Close connection
cursor.close()
connection.close()

