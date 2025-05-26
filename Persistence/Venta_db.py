# --- venta_db.py ---
from Persistence.ConexionBD import obtener_conexion

def insertar_venta(fecha_hora, descuento, iva, total, id_empleado, id_cliente, id_formapago):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO venta (Fecha_Hora, Descuento, IVA, Total, Empleado_idEmpleado, Cliente_idTelefono, FormaPago_idFormaPago)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (fecha_hora, descuento, iva, total, id_empleado, id_cliente, id_formapago))
    conn.commit()
    id_generado = cursor.lastrowid
    cursor.close()
    conn.close()
    return id_generado

def insertar_detalle_venta(cantidad, precio_unitario, subtotal, id_producto, id_venta):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO detalles_venta (Cantidad, PrecioUnitario, Subtotal, Producto_idCodigo, Venta_idVenta)
        VALUES (%s, %s, %s, %s, %s)
    """, (cantidad, precio_unitario, subtotal, id_producto, id_venta))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_ventas():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.idVenta, v.Fecha_Hora, v.Total, c.Nombres, f.Nombre, e.Nombres
        FROM venta v
        JOIN cliente c ON v.Cliente_idTelefono = c.idTelefono
        JOIN formapago f ON v.FormaPago_idFormaPago = f.idFormaPago
        JOIN empleado e ON v.Empleado_idEmpleado = e.idEmpleado
    """)
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos

