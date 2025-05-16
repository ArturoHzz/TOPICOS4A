from Persistence.ConexionBD import obtener_conexion

def obtener_formas_pago(orden="id"):
    conn = obtener_conexion()
    cursor = conn.cursor()

    if orden == "id_asc":
        query = "SELECT * FROM formapago ORDER BY idFormaPago ASC"
    elif orden == "id_desc":
        query = "SELECT * FROM formapago ORDER BY idFormaPago DESC"
    elif orden == "nombre":
        query = "SELECT * FROM formapago ORDER BY Nombre ASC"
    else:
        query = "SELECT * FROM formapago"

    cursor.execute(query)
    formas = cursor.fetchall()
    cursor.close()
    conn.close()
    return formas

def insertar_forma_pago(id_forma, nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO formapago (idFormaPago, Nombre) VALUES (%s, %s)",
        (id_forma, nombre)
    )
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_forma_pago(id_forma, nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE formapago SET Nombre = %s WHERE idFormaPago = %s",
        (nombre, id_forma)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_forma_pago(id_forma):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM formapago WHERE idFormaPago = %s", (id_forma,))
    conn.commit()
    cursor.close()
    conn.close()
