import flet as ft
from Persistence.Producto_db import insertar_producto, obtener_productos, actualizar_producto, eliminar_producto
from Persistence.Categoria_db import obtener_categorias
from Persistence.Unidad_db import obtener_unidades

def producto_view(page: ft.Page):
    txt_id = ft.TextField(label="ID Producto (13 dígitos)", max_length=14)
    txt_nombre = ft.TextField(label="Nombre")
    txt_contenido = ft.TextField(label="Contenido")
    txt_costo = ft.TextField(label="Costo Unitario")
    txt_precio = ft.TextField(label="Precio Unitario")
    txt_existencia = ft.TextField(label="Existencia")
    chk_activo = ft.Checkbox(label="Activo")

    ddl_categoria = ft.Dropdown(label="Categoría", options=[])
    ddl_unidad = ft.Dropdown(label="Unidad", options=[])

    def cargar_dropdowns():
        ddl_categoria.options.clear()
        ddl_unidad.options.clear()
        for idc, nombre in obtener_categorias():
            ddl_categoria.options.append(ft.dropdown.Option(str(idc), nombre))
        for idu, nombre, _ in obtener_unidades():
            ddl_unidad.options.append(ft.dropdown.Option(str(idu), nombre))
        page.update()

    def limpiar():
        txt_id.value = ""
        txt_nombre.value = ""
        txt_contenido.value = ""
        txt_costo.value = ""
        txt_precio.value = ""
        txt_existencia.value = ""
        chk_activo.value = False
        ddl_categoria.value = None
        ddl_unidad.value = None
        page.update()

    def guardar(e):
        try:
            if txt_id.value.strip() == "" or len(txt_id.value.strip()) != 13:
                page.snack_bar = ft.SnackBar(ft.Text("ID debe tener exactamente 13 caracteres"), open=True)
                page.update()
                return
            if not ddl_categoria.value or not ddl_unidad.value:
                page.snack_bar = ft.SnackBar(ft.Text("Selecciona una categoría y unidad"), open=True)
                page.update()
                return

            insertar_producto(
                txt_id.value.strip(),
                txt_nombre.value.strip(),
                int(txt_contenido.value),
                float(txt_costo.value),
                float(txt_precio.value),
                int(txt_existencia.value),
                1 if chk_activo.value else 0,
                int(ddl_categoria.value),
                int(ddl_unidad.value)
            )
            limpiar()
            cargar_productos()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error al guardar: {ex}"), open=True)
            page.update()

    def cargar_productos():
        data_table.rows.clear()
        for p in obtener_productos():
            data_table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(p[0]))),
                ft.DataCell(ft.Text(p[1])),
                ft.DataCell(ft.Text(str(p[2]))),
                ft.DataCell(ft.Text(str(p[3]))),
                ft.DataCell(ft.Text(str(p[4]))),
                ft.DataCell(ft.Text(str(p[5]))),
                ft.DataCell(ft.Text("Activo" if p[6] == 1 else "Inactivo"))
            ]))
        page.update()

    data_table = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("ID")),
        ft.DataColumn(label=ft.Text("Nombre")),
        ft.DataColumn(label=ft.Text("Contenido")),
        ft.DataColumn(label=ft.Text("Costo U.")),
        ft.DataColumn(label=ft.Text("Precio U.")),
        ft.DataColumn(label=ft.Text("Existencia")),
        ft.DataColumn(label=ft.Text("Estado")),
    ], rows=[])

    cargar_dropdowns()
    cargar_productos()

    return ft.View("/producto", [
        ft.Text("Gestión de Productos", size=30, weight="bold"),
        txt_id, txt_nombre, txt_contenido,
        txt_costo, txt_precio, txt_existencia,
        chk_activo, ddl_categoria, ddl_unidad,
        ft.ElevatedButton("Guardar", on_click=guardar),
        ft.Container(content=ft.Column([data_table], scroll=ft.ScrollMode.ALWAYS), height=300),
        ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/"))
    ], scroll=ft.ScrollMode.ALWAYS)

