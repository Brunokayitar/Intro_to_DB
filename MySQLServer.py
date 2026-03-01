import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       # your password if any
        database="your_db_name"  # replace with your database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")