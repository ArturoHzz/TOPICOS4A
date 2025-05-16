from Persistence.ConexionBD import obtener_conexion

def obtener_cliente(orden="id"):
    conn = obtener_conexion()
    cursor = conn.cursor()

    if orden == "id_asc":
        query = "SELECT * FROM cliente ORDER BY idTelefono ASC"
    elif orden == "id_desc":
        query = "SELECT * FROM cliente ORDER BY idTelefono DESC"
    elif orden == "apellido":
        query = "SELECT * FROM cliente ORDER BY Apellidos ASC"
    else:
        query = "SELECT * FROM cliente"

    cursor.execute(query)
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes

def insertar_cliente(id_cliente, nombres, apellidos, correo):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cliente (idTelefono, Nombres, Apellidos, Correo) VALUES (%s, %s, %s, %s)",
        (id_cliente, nombres, apellidos, correo)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_cliente_id(id_cliente):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cliente WHERE idTelefono = %s", (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_cliente_id(id_cliente, nombres, apellidos, correo):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cliente SET Nombres = %s, Apellidos = %s, Correo = %s WHERE idTelefono = %s",
        (nombres, apellidos, correo, id_cliente)
    )
    conn.commit()
    cursor.close()
    conn.close()

