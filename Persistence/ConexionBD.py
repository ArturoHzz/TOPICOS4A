import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dex234feR",
            database="dbfarmacia"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None