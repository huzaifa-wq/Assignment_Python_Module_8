import mysql.connector
from geopy.distance import geodesic


connection = mysql.connector.connect(
    port= 3306,
    host='127.0.0.1',
    user="huzaifa",
    password="huzaifa",
    database="flight_game",
    autocommit=True
)

cursor = connection.cursor()

# Ask user for ICAO codes
icao1 = input("Enter first ICAO code: ").upper()
icao2 = input("Enter second ICAO code: ").upper()

# SQL query to get coordinates
sql = """
SELECT latitude_deg, longitude_deg
FROM airport
WHERE ident = %s
"""

# Fetch first airport
cursor.execute(sql, (icao1,))
airport1 = cursor.fetchone()

# Fetch second airport
cursor.execute(sql, (icao2,))
airport2 = cursor.fetchone()

# Check if both airports exist
if airport1 and airport2:
    coord1 = (airport1[0], airport1[1])
    coord2 = (airport2[0], airport2[1])

    distance = geodesic(coord1, coord2).kilometers

    print(f"Distance between {icao1} and {icao2}: {distance:.2f} km")
else:
    print("One or both ICAO codes were not found.")

# Close connection
cursor.close()
connection.close()
