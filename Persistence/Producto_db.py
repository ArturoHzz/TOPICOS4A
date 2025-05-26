from Persistence.ConexionBD import obtener_conexion

def obtener_productos(orden="id"):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return productos

def insertar_producto(idCodigo, nombre, contenido, costoU, precioU, existencia, activo, categoria, unidad):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO producto (idCodigo, Nombre, Contenido, CostoUnitario, PrecioUnitario, Existencia, Activo, Categoria_idCategoria, Unidad_idUnidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (idCodigo, nombre, contenido, costoU, precioU, existencia, activo, categoria, unidad)
    )
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_producto(idCodigo, nombre, contenido, costoU, precioU, existencia, activo, categoria, unidad):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE producto SET Nombre = %s, Contenido = %s, CostoUnitario = %s, PrecioUnitario = %s, Existencia = %s, Activo = %s, Categoria_idCategoria = %s, Unidad_idUnidad = %s WHERE idCodigo = %s",
        (nombre, contenido, costoU, precioU, existencia, activo, categoria, unidad, idCodigo)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_producto(idCodigo):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE idCodigo = %s", (idCodigo,))
    conn.commit()
    cursor.close()
    conn.close()

def aumentar_existencia(id_producto, cantidad):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE producto SET Existencia = Existencia + %s WHERE idCodigo = %s", (cantidad, id_producto))
    conn.commit()
    cursor.close()
    conn.close()

def disminuir_existencia(id_producto, cantidad):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE producto SET Existencia = Existencia - %s WHERE idCodigo = %s", (cantidad, id_producto))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_producto_por_codigo(codigo_barras):
    """
    Busca un producto por su código de barras
    
    Args:
        codigo_barras (str): El código de barras a buscar
        
    Returns:
        tuple: Los datos del producto (id, nombre, precio, codigo_barras, existencia, ...)
        None: Si no se encuentra el producto
    """
    try:
        cursor = obtener_conexion.cursor()
        
        # Ajusta esta consulta según la estructura de tu tabla productos
        # Asumiendo que tienes columnas: id, nombre, precio, codigo_barras, existencia
        query = """
            SELECT id, nombre, precio, codigo_barras, existencia 
            FROM productos 
            WHERE codigo_barras = ?
        """
        
        cursor.execute(query, (codigo_barras,))
        resultado = cursor.fetchone()
        cursor.close()
        
        return resultado
        
    except Exception as e:
        print(f"Error al buscar producto por código: {e}")
        return None
