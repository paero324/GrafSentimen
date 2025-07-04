import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",         # Ganti ke nama host server DB kamu
        user="root",              # Ganti dengan user DB kamu
        password="",      # Ganti dengan password DB kamu
        database="grafsentimen"   # Pastikan sesuai nama database kamu
    )
