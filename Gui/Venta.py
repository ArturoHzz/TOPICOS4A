import flet as ft
from datetime import datetime
from Persistence.Venta_db import insertar_venta, insertar_detalle_venta, obtener_ventas
from Persistence.Empleado_db import obtener_empleados
from Persistence.Cliente_db import obtener_cliente
from Persistence.FormaPago_db import obtener_formas_pago
from Persistence.Producto_db import obtener_productos, disminuir_existencia, obtener_producto_por_codigo

def venta_view(page: ft.Page):
    txt_descuento = ft.TextField(label="Descuento", value="0.00")
    txt_iva = ft.TextField(label="IVA", value="0.00")
    txt_total = ft.TextField(label="Total", value="0.00", read_only=True)
    dropdown_empleado = ft.Dropdown(label="Empleado", options=[])
    dropdown_cliente = ft.Dropdown(label="Cliente", options=[])
    dropdown_forma_pago = ft.Dropdown(label="Forma de Pago", options=[])
    dropdown_producto = ft.Dropdown(label="Producto", options=[])


    txt_codigo_barras = ft.TextField(
        label="Código de Barras (F1 para enfocar)",
        hint_text="Escanea o escribe el código de barras",
        on_submit=lambda e: buscar_producto_por_codigo(),
        autofocus=False,
        border_color=ft.colors.BLUE_400
    )

    txt_cantidad = ft.TextField(label="Cantidad", value="1")


    txt_producto_info = ft.Text(
        value="",
        size=14,
        color=ft.colors.GREEN_700,
        weight="bold"
    )

    detalle_table = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("Producto")),
        ft.DataColumn(label=ft.Text("Código")),
        ft.DataColumn(label=ft.Text("Cantidad")),
        ft.DataColumn(label=ft.Text("Precio U.")),
        ft.DataColumn(label=ft.Text("Subtotal")),
        ft.DataColumn(label=ft.Text("Acción")),
    ], rows=[])

    detalles_venta = []

    def cargar_dropdowns():
        dropdown_empleado.options = [ft.dropdown.Option(str(e[0]), e[1]) for e in obtener_empleados("nombreApellido")]
        dropdown_cliente.options = [ft.dropdown.Option(str(c[0]), c[1]) for c in obtener_cliente()]
        dropdown_forma_pago.options = [ft.dropdown.Option(str(fp[0]), fp[1]) for fp in obtener_formas_pago()]
        dropdown_producto.options = [ft.dropdown.Option(str(p[0]), p[1]) for p in obtener_productos()]
        page.update()

    def buscar_producto_por_codigo():
        """Busca un producto por código de barras y lo agrega automáticamente"""
        try:
            codigo = txt_codigo_barras.value.strip()
            if not codigo:
                return
            

            producto = obtener_producto_por_codigo(codigo)
            
            if producto:

                id_producto = producto[0]
                nombre_producto = producto[1]
                precio_producto = float(producto[2])  
                existencia = producto[4] if len(producto) > 4 else 0  
                

                if existencia <= 0:
                    txt_producto_info.value = f"❌ Producto '{nombre_producto}' sin existencia"
                    txt_producto_info.color = ft.colors.RED_700
                    txt_codigo_barras.value = ""
                    page.update()
                    return
                

                producto_existente = next((d for d in detalles_venta if d[0] == str(id_producto)), None)
                
                if producto_existente:

                    incrementar_cantidad_producto(str(id_producto))
                    txt_producto_info.value = f"✅ Cantidad incrementada: {nombre_producto}"
                else:

                    cantidad = float(txt_cantidad.value or 1)
                    

                    if cantidad > existencia:
                        txt_producto_info.value = f"❌ Cantidad solicitada ({cantidad}) excede existencia ({existencia})"
                        txt_producto_info.color = ft.colors.RED_700
                        txt_codigo_barras.value = ""
                        page.update()
                        return
                    
                    subtotal = cantidad * precio_producto
                    

                    detalles_venta.append((str(id_producto), nombre_producto, cantidad, precio_producto, subtotal, codigo))
                    

                    detalle_table.rows.append(ft.DataRow(cells=[
                        ft.DataCell(ft.Text(nombre_producto)),
                        ft.DataCell(ft.Text(codigo)),
                        ft.DataCell(ft.Text(str(cantidad))),
                        ft.DataCell(ft.Text(f"{precio_producto:.2f}")),
                        ft.DataCell(ft.Text(f"{subtotal:.2f}")),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color=ft.colors.RED,
                                tooltip="Eliminar",
                                on_click=lambda e, idx=len(detalles_venta)-1: eliminar_detalle(idx)
                            )
                        )
                    ]))
                    
                    txt_producto_info.value = f"✅ Agregado: {nombre_producto} - Cantidad: {cantidad}"
                
                txt_producto_info.color = ft.colors.GREEN_700
                actualizar_total()
                

                txt_codigo_barras.value = ""
                txt_codigo_barras.focus()
                
            else:
                txt_producto_info.value = f"❌ Producto no encontrado: {codigo}"
                txt_producto_info.color = ft.colors.RED_700
                txt_codigo_barras.value = ""
            
            page.update()
            
        except Exception as ex:
            print(f"Error buscando producto: {ex}")
            txt_producto_info.value = f"❌ Error: {ex}"
            txt_producto_info.color = ft.colors.RED_700
            txt_codigo_barras.value = ""
            page.update()

    def incrementar_cantidad_producto(id_producto):
        """Incrementa la cantidad de un producto ya existente en el detalle"""
        for i, detalle in enumerate(detalles_venta):
            if detalle[0] == id_producto:
                nueva_cantidad = detalle[2] + 1
                nuevo_subtotal = nueva_cantidad * detalle[3]
                

                detalles_venta[i] = (detalle[0], detalle[1], nueva_cantidad, detalle[3], nuevo_subtotal, detalle[5])
                

                detalle_table.rows[i].cells[2] = ft.DataCell(ft.Text(str(nueva_cantidad)))
                detalle_table.rows[i].cells[4] = ft.DataCell(ft.Text(f"{nuevo_subtotal:.2f}"))
                break

    def eliminar_detalle(index):
        """Elimina un producto del detalle de venta"""
        try:
            if 0 <= index < len(detalles_venta):
                producto_eliminado = detalles_venta[index][1]
                del detalles_venta[index]
                del detalle_table.rows[index]
                

                for i, row in enumerate(detalle_table.rows):
                    if len(row.cells) > 5:  
                        row.cells[5] = ft.DataCell(
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color=ft.colors.RED,
                                tooltip="Eliminar",
                                on_click=lambda e, idx=i: eliminar_detalle(idx)
                            )
                        )
                
                actualizar_total()
                txt_producto_info.value = f"🗑️ Eliminado: {producto_eliminado}"
                txt_producto_info.color = ft.colors.ORANGE_700
                page.update()
        except Exception as ex:
            print(f"Error eliminando detalle: {ex}")

    def agregar_detalle(e):
        """Método manual para agregar productos (dropdown) usando el precio del producto"""
        try:
            id_producto = dropdown_producto.value
            if not id_producto:
                raise ValueError("Selecciona un producto")

            cantidad = float(txt_cantidad.value or 1)
            if cantidad <= 0:
                raise ValueError("Cantidad debe ser mayor a 0")

            # Buscar producto completo por ID para obtener precio y código
            productos = obtener_productos()
            producto_seleccionado = next(p for p in productos if str(p[0]) == id_producto)
            nombre_producto = producto_seleccionado[1]
            precio_unit = float(producto_seleccionado[2])  # PrecioUnitario
            codigo_barras = producto_seleccionado[3] if len(producto_seleccionado) > 3 else "N/A"
            existencia = int(producto_seleccionado[5]) if len(producto_seleccionado) > 5 else 0

            if cantidad > existencia:
                raise ValueError(f"Cantidad ({cantidad}) excede existencia ({existencia})")

            subtotal = cantidad * precio_unit

            detalles_venta.append((id_producto, nombre_producto, cantidad, precio_unit, subtotal, codigo_barras))
            detalle_table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(nombre_producto)),
                ft.DataCell(ft.Text(codigo_barras)),
                ft.DataCell(ft.Text(str(cantidad))),
                ft.DataCell(ft.Text(f"{precio_unit:.2f}")),
                ft.DataCell(ft.Text(f"{subtotal:.2f}")),
                ft.DataCell(
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color=ft.colors.RED,
                        tooltip="Eliminar",
                        on_click=lambda e, idx=len(detalles_venta)-1: eliminar_detalle(idx)
                    )
                )
            ]))

            txt_cantidad.value = "1"
            dropdown_producto.value = None
            actualizar_total()
            page.update()

        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error al agregar detalle: {ex}"), open=True)
            page.update()

    def actualizar_total():
        try:
            total = sum(d[4] for d in detalles_venta)
            txt_total.value = f"{total:.2f}"
            page.update()
        except Exception as ex:
            txt_total.value = "0.00"
            print(f"Error actualizando total: {ex}")

    def guardar_venta(e):
        try:
            if not detalles_venta:
                raise ValueError("Agrega al menos un producto")
            if not dropdown_empleado.value or not dropdown_forma_pago.value:
                raise ValueError("Selecciona empleado y forma de pago")
            
            descuento = float(txt_descuento.value)
            iva = float(txt_iva.value)
            total = float(txt_total.value)
            empleado = int(dropdown_empleado.value)
            cliente = dropdown_cliente.value
            forma_pago = int(dropdown_forma_pago.value)
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            id_venta = insertar_venta(fecha, descuento, iva, total, empleado, cliente, forma_pago)
            for d in detalles_venta:
                insertar_detalle_venta(d[2], d[3], d[4], d[0], id_venta)
                disminuir_existencia(d[0], d[2])

            page.snack_bar = ft.SnackBar(ft.Text("¡Venta registrada exitosamente!"), open=True)
            cargar_tabla_ventas()
            limpiar()
            
        except Exception as ex:
            import traceback
            traceback.print_exc()
            page.snack_bar = ft.SnackBar(ft.Text(f"Error al guardar: {ex}"), open=True)
            page.update()

    def limpiar():
        txt_descuento.value = "0.00"
        txt_iva.value = "0.00"
        txt_total.value = "0.00"
        dropdown_empleado.value = None
        dropdown_cliente.value = None
        dropdown_forma_pago.value = None
        dropdown_producto.value = None
        txt_cantidad.value = "1"
        txt_codigo_barras.value = ""
        txt_producto_info.value = ""
        detalle_table.rows.clear()
        detalles_venta.clear()
        page.update()

    def enfocar_scanner(e):
        """Enfoca el campo del escáner de código de barras"""
        txt_codigo_barras.focus()


    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "F1":
            enfocar_scanner(e)
        elif e.key == "F2" and txt_codigo_barras.focused:
            buscar_producto_por_codigo()

    page.on_keyboard_event = on_keyboard

    data_table = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("ID Venta")),
        ft.DataColumn(label=ft.Text("Fecha-Hora")),
        ft.DataColumn(label=ft.Text("Total")),
        ft.DataColumn(label=ft.Text("Cliente")),
        ft.DataColumn(label=ft.Text("Pago")),
        ft.DataColumn(label=ft.Text("Empleado"))
    ], rows=[])

    def cargar_tabla_ventas():
        try:
            data_table.rows.clear()
            for v in obtener_ventas():
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(v[0]))),
                    ft.DataCell(ft.Text(str(v[1]))),
                    ft.DataCell(ft.Text(f"{v[2]:.2f}")),
                    ft.DataCell(ft.Text(str(v[3]) if v[3] else "Sin cliente")),
                    ft.DataCell(ft.Text(str(v[4]))),
                    ft.DataCell(ft.Text(str(v[5])))
                ]))
            page.update()
        except Exception as ex:
            print(f"Error cargando tabla de ventas: {ex}")

    cargar_dropdowns()
    cargar_tabla_ventas()

    return ft.View("/venta", [
        ft.Text("Registro de Venta", size=30, weight="bold"),
        
        ft.Row([dropdown_empleado, dropdown_cliente, dropdown_forma_pago]),
        ft.Row([txt_descuento, txt_iva, txt_total]),
        
        ft.Divider(),

        ft.Container(
            content=ft.Column([
                ft.Text("Escáner de Código de Barras", size=18, weight="bold", color=ft.colors.BLUE_700),
                ft.Row([
                    txt_codigo_barras,
                    ft.ElevatedButton(
                        "🔍 Buscar",
                        on_click=lambda e: buscar_producto_por_codigo(),
                        bgcolor=ft.colors.BLUE,
                        color=ft.colors.WHITE
                    ),
                    ft.ElevatedButton(
                        "F1",
                        on_click=enfocar_scanner,
                        bgcolor=ft.colors.GREY,
                        color=ft.colors.WHITE,
                        tooltip="Presiona F1 para enfocar scanner"
                    )
                ]),
                ft.Row([
                    txt_cantidad,
                    txt_producto_info
                ])
            ]),
            padding=10,
            border_radius=10,
            border=ft.border.all(2, ft.colors.BLUE_200)
        ),
        
        ft.Divider(),
        
        # Método manual (dropdown)
        ft.Text("Agregar Manualmente", size=18, weight="bold"),
        ft.Row([dropdown_producto]),
        ft.ElevatedButton("Agregar Detalle", on_click=agregar_detalle),
        
        ft.Divider(),
        

        ft.Text("Detalle de la Venta", size=18, weight="bold"),
        ft.Container(
            content=ft.Column([detalle_table], scroll=ft.ScrollMode.ALWAYS), 
            height=250,
            border=ft.border.all(1, ft.colors.GREY_400)
        ),

        ft.Row([
            ft.ElevatedButton(
                "Guardar Venta", 
                on_click=guardar_venta, 
                bgcolor=ft.colors.GREEN, 
                color=ft.colors.WHITE,
                width=150
            ),
            ft.ElevatedButton(
                "Limpiar", 
                on_click=lambda e: limpiar(), 
                bgcolor=ft.colors.ORANGE, 
                color=ft.colors.WHITE,
                width=150
            )
        ]),
        
        ft.Divider(),
        ft.Text("Ventas Registradas", size=18, weight="bold"),
        ft.Container(
            content=ft.Column([data_table], scroll=ft.ScrollMode.ALWAYS), 
            height=250,
            border=ft.border.all(1, ft.colors.GREY_400)
        ),
        ft.ElevatedButton(
            "Volver al menú", 
            on_click=lambda e: page.go("/"), 
            bgcolor=ft.colors.GREY,
            color=ft.colors.WHITE
        )
    ], scroll=ft.ScrollMode.ALWAYS)