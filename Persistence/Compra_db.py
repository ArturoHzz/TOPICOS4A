# --- compra_db.py ---
from Persistence.ConexionBD import obtener_conexion

def insertar_compra(fecha, total, observaciones, proveedor_id, empleado_id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO compra (Fecha, Total, Observaciones, Proveedor_idProveedor, Empleado_idEmpleado)
        VALUES (%s, %s, %s, %s, %s)
    """, (fecha, total, observaciones, proveedor_id, empleado_id))
    conn.commit()
    id_generado = cursor.lastrowid
    cursor.close()
    conn.close()
    return id_generado

def insertar_detalle_compra(cantidad, costo_unitario, id_compra, id_producto):
    conn = obtener_conexion()
    cursor = conn.cursor()
    subtotal = cantidad * costo_unitario
    cursor.execute("""
        INSERT INTO detallescompra (Cantidad, CostoUnitario, Compra_idCompra, Producto_idCodigo)
        VALUES (%s, %s, %s, %s)
    """, (cantidad, costo_unitario, id_compra, id_producto))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_compras():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.idCompra, c.Fecha, c.Total, p.Nombre, e.Nombres, c.Observaciones
        FROM compra c
        JOIN proveedor p ON c.Proveedor_idProveedor = p.idProveedor
        JOIN empleado e ON c.Empleado_idEmpleado = e.idEmpleado
    """)
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos

