from Persistence.ConexionBD import obtener_conexion

def obtener_unidades(orden="id"):
    conn = obtener_conexion()
    cursor = conn.cursor()

    if orden == "id_asc":
        query = "SELECT * FROM unidad ORDER BY idUnidad ASC"
    elif orden == "id_desc":
        query = "SELECT * FROM unidad ORDER BY idUnidad DESC"
    elif orden == "nombre":
        query = "SELECT * FROM unidad ORDER BY Nombre ASC"
    else:
        query = "SELECT * FROM unidad"

    cursor.execute(query)
    unidades = cursor.fetchall()
    cursor.close()
    conn.close()
    return unidades

def insertar_unidad(id_unidad, nombre, abreviatura):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO unidad (idUnidad, Nombre, Abreviatura) VALUES (%s, %s, %s)",
        (id_unidad, nombre, abreviatura)
    )
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_unidad(id_unidad, nombre, abreviatura):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE unidad SET Nombre = %s, Abreviatura = %s WHERE idUnidad = %s",
        (nombre, abreviatura, id_unidad)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_unidad(id_unidad):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM unidad WHERE idUnidad = %s", (id_unidad,))
    conn.commit()
    cursor.close()
    conn.close()
