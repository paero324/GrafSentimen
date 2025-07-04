import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",         # atau nama host DB kamu
        user="root",              # user MySQL kamu
        password="yourpassword",  # password MySQL kamu
        database="grafsentimen"   # nama database kamu
    )
