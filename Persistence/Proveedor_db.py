from Persistence.ConexionBD import obtener_conexion

def obtener_proveedores(orden="id"):
    conn = obtener_conexion()
    cursor = conn.cursor()

    if orden == "id_asc":
        query = "SELECT * FROM proveedor ORDER BY idProveedor ASC"
    elif orden == "id_desc":
        query = "SELECT * FROM proveedor ORDER BY idProveedor DESC"
    elif orden == "nombre":
        query = "SELECT * FROM proveedor ORDER BY Nombre ASC"
    else:
        query = "SELECT * FROM proveedor"

    cursor.execute(query)
    proveedores = cursor.fetchall()
    cursor.close()
    conn.close()
    return proveedores

def insertar_proveedor(id_prov, nombre, telefono, email, direccion, rfc):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO proveedor (idProveedor, Nombre, Telefono, Email, Direccion, Rfc) VALUES (%s, %s, %s, %s, %s, %s)",
        (id_prov, nombre, telefono, email, direccion, rfc)
    )
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_proveedor(id_prov, nombre, telefono, email, direccion, rfc):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE proveedor SET Nombre = %s, Telefono = %s, Email = %s, Direccion = %s, Rfc = %s WHERE idProveedor = %s",
        (nombre, telefono, email, direccion, rfc, id_prov)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_proveedor(id_prov):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM proveedor WHERE idProveedor = %s", (id_prov,))
    conn.commit()
    cursor.close()
    conn.close()
