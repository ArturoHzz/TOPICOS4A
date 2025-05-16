from Persistence.ConexionBD import obtener_conexion

def obtener_categorias(orden="id"):
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    if orden == "id_asc":
        query = "SELECT * FROM categoria ORDER BY idCategoria ASC"
    elif orden == "id_desc":
        query = "SELECT * FROM categoria ORDER BY idCategoria DESC"
    elif orden == "nombre":
        query = "SELECT * FROM categoria ORDER BY Nombre ASC"
    else:
        query = "SELECT * FROM categoria"
    
    cursor.execute(query)
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()
    return categorias

def insertar_categoria(id_categoria, nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categoria (idCategoria, Nombre) VALUES (%s, %s)", (id_categoria, nombre))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_categoria_por_id(id_categoria):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categoria WHERE idCategoria = %s", (id_categoria,))
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_categoria_por_id(id_categoria, nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE categoria SET Nombre = %s WHERE idCategoria = %s", (nombre, id_categoria))
    conn.commit()
    cursor.close()
    conn.close()
