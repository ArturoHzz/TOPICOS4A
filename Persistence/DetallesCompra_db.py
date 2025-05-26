from Persistence.ConexionBD import obtener_conexion

def insertar_detalle_compra(id_detalle, cantidad, costo_unitario, id_compra, id_producto):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO detallescompra (idDetallesCompra, Cantidad, CostoUnitario, Compra_idCompra, Producto_idCodigo)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_detalle, cantidad, costo_unitario, id_compra, id_producto))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_detalles_por_compra(id_compra):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            dc.idDetallesCompra,
            dc.Cantidad,
            dc.CostoUnitario,
            p.Nombre,
            dc.Producto_idCodigo
        FROM detallescompra dc
        JOIN producto p ON dc.Producto_idCodigo = p.idCodigo
        WHERE dc.Compra_idCompra = %s
    """, (id_compra,))
    detalles = cursor.fetchall()
    cursor.close()
    conn.close()
    return detalles

def eliminar_detalle_compra(id_detalle):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM detallescompra WHERE idDetallesCompra = %s", (id_detalle,))
    conn.commit()
    cursor.close()
    conn.close()
