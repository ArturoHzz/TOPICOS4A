import flet as ft
from datetime import date
from Persistence.Compra_db import insertar_compra, insertar_detalle_compra, obtener_compras
from Persistence.Empleado_db import obtener_empleados
from Persistence.Proveedor_db import obtener_proveedores
from Persistence.Producto_db import obtener_productos, aumentar_existencia

def compra_view(page: ft.Page):
    txt_total = ft.TextField(label="Total", value="0.00", read_only=True)
    txt_observaciones = ft.TextField(label="Observaciones")
    fecha_actual = date.today().strftime("%Y-%m-%d")
    txt_fecha = ft.TextField(label="Fecha", value=fecha_actual, read_only=True)

    dropdown_empleado = ft.Dropdown(label="Empleado", options=[])
    dropdown_proveedor = ft.Dropdown(label="Proveedor", options=[])
    dropdown_producto = ft.Dropdown(label="Producto", options=[])

    txt_cantidad = ft.TextField(label="Cantidad")
    txt_costo_unitario = ft.TextField(label="Costo Unitario")

    detalle_table = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("Producto")),
        ft.DataColumn(label=ft.Text("Cantidad")),
        ft.DataColumn(label=ft.Text("Costo U.")),
        ft.DataColumn(label=ft.Text("Subtotal")),
    ], rows=[])

    detalles_compra = []

    def cargar_dropdowns():
        dropdown_empleado.options = [ft.dropdown.Option(str(e[0]), e[1]) for e in obtener_empleados("nombreApellido")]
        dropdown_proveedor.options = [ft.dropdown.Option(str(p[0]), p[1]) for p in obtener_proveedores("nombre_id")]
        dropdown_producto.options = [ft.dropdown.Option(str(p[0]), p[1]) for p in obtener_productos()]
        page.update()

    def agregar_detalle(e):
        try:
            if not dropdown_producto.value:
                raise ValueError("Selecciona un producto")
            cantidad = float(txt_cantidad.value)
            costo = float(txt_costo_unitario.value)
            if cantidad <= 0 or costo <= 0:
                raise ValueError("Cantidad y costo deben ser mayores a 0")
            nombre_producto = next(p.text for p in dropdown_producto.options if p.key == dropdown_producto.value)
            subtotal = cantidad * costo
            detalles_compra.append((dropdown_producto.value, nombre_producto, cantidad, costo, subtotal))
            detalle_table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(nombre_producto)),
                ft.DataCell(ft.Text(str(cantidad))),
                ft.DataCell(ft.Text(f"{costo:.2f}")),
                ft.DataCell(ft.Text(f"{subtotal:.2f}"))
            ]))
            txt_cantidad.value = ""
            txt_costo_unitario.value = ""
            dropdown_producto.value = None
            actualizar_total()
            page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error al agregar detalle: {ex}"), open=True)
            page.update()

    def actualizar_total():
        try:
            total = sum(d[4] for d in detalles_compra)
            txt_total.value = f"{total:.2f}"
            page.update()
        except Exception as ex:
            txt_total.value = "0.00"
            print(f"Error actualizando total: {ex}")

    def guardar_compra(e):
        try:
            if not detalles_compra:
                raise ValueError("Debes agregar al menos un producto")
            if not dropdown_empleado.value or not dropdown_proveedor.value:
                raise ValueError("Selecciona proveedor y empleado")
            total = float(txt_total.value)
            id_empleado = int(dropdown_empleado.value)
            id_proveedor = int(dropdown_proveedor.value)
            id_compra = insertar_compra(fecha_actual, total, txt_observaciones.value, id_proveedor, id_empleado)
            for d in detalles_compra:
                insertar_detalle_compra(d[2], d[3], id_compra, d[0])
                aumentar_existencia(d[0], d[2])
            page.snack_bar = ft.SnackBar(ft.Text("¡Compra registrada exitosamente!"), open=True)
            cargar_tabla_compras()
            limpiar()
        except Exception as ex:
            import traceback
            traceback.print_exc()
            page.snack_bar = ft.SnackBar(ft.Text(f"Error al guardar: {ex}"), open=True)
            page.update()

    def limpiar():
        txt_total.value = "0.00"
        txt_observaciones.value = ""
        dropdown_empleado.value = None
        dropdown_proveedor.value = None
        dropdown_producto.value = None
        txt_cantidad.value = ""
        txt_costo_unitario.value = ""
        detalle_table.rows.clear()
        detalles_compra.clear()
        page.update()

    data_table = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("ID Compra")),
        ft.DataColumn(label=ft.Text("Fecha")),
        ft.DataColumn(label=ft.Text("Total")),
        ft.DataColumn(label=ft.Text("Proveedor")),
        ft.DataColumn(label=ft.Text("Empleado")),
        ft.DataColumn(label=ft.Text("Observaciones"))
    ], rows=[])

    def cargar_tabla_compras():
        try:
            data_table.rows.clear()
            for c in obtener_compras():
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(c[0]))),
                    ft.DataCell(ft.Text(c[1])),
                    ft.DataCell(ft.Text(f"{c[2]:.2f}")),
                    ft.DataCell(ft.Text(c[3])),
                    ft.DataCell(ft.Text(c[4])),
                    ft.DataCell(ft.Text(c[5] or ""))
                ]))
            page.update()
        except Exception as ex:
            print(f"Error cargando compras: {ex}")

    cargar_dropdowns()
    cargar_tabla_compras()

    return ft.View("/compra", [
        ft.Text("Registro de Compra", size=30, weight="bold"),
        ft.Row([txt_fecha, dropdown_empleado, dropdown_proveedor]),
        txt_observaciones,
        ft.Row([txt_total]),
        ft.Divider(),
        ft.Text("Detalle de la Compra", size=18, weight="bold"),
        ft.Row([dropdown_producto, txt_cantidad, txt_costo_unitario]),
        ft.ElevatedButton("Agregar Detalle", on_click=agregar_detalle),
        ft.Container(content=ft.Column([detalle_table], scroll=ft.ScrollMode.ALWAYS), height=200),
        ft.Row([
            ft.ElevatedButton("Guardar Compra", on_click=guardar_compra, bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            ft.ElevatedButton("Limpiar", on_click=lambda e: limpiar(), bgcolor=ft.colors.ORANGE, color=ft.colors.WHITE)
        ]),
        ft.Divider(),
        ft.Text("Compras Registradas", size=18, weight="bold"),
        ft.Container(content=ft.Column([data_table], scroll=ft.ScrollMode.ALWAYS), height=250),
        ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/"), bgcolor=ft.colors.GREY)
    ], scroll=ft.ScrollMode.ALWAYS)













    

        