from Persistence.ConexionBD import obtener_conexion

def obtener_empleados(orden="id"):
    conn = obtener_conexion()
    cursor = conn.cursor()

    if orden == "id_asc":
        query = "SELECT * FROM empleado ORDER BY idEmpleado ASC"
    elif orden == "id_desc":
        query = "SELECT * FROM empleado ORDER BY idEmpleado DESC"
    elif orden == "apellido":
        query = "SELECT * FROM empleado ORDER BY Apellidos ASC"
    elif orden == "nombreApellido":
        query = "SELECT idEmpleado, CONCAT(Nombres, ' ', Apellidos) nombre_completo FROM empleado"
    else:
        query = "SELECT * FROM empleado"

    cursor.execute(query)
    empleados = cursor.fetchall()
    cursor.close()
    conn.close()
    return empleados

def insertar_empleado(id_empleado, nombres, apellidos, rfc):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO empleado (idEmpleado, Nombres, Apellidos, RFC) VALUES (%s, %s, %s, %s)",
        (id_empleado, nombres, apellidos, rfc)
    )
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_empleado_id(id_empleado, nombres, apellidos, rfc):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE empleado SET Nombres = %s, Apellidos = %s, RFC = %s WHERE idEmpleado = %s",
        (nombres, apellidos, rfc, id_empleado)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_empleado_id(id_empleado):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM empleado WHERE idEmpleado = %s", (id_empleado,))
    conn.commit()
    cursor.close()
    conn.close()
