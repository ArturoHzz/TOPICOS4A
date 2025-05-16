import flet as ft
from Persistence.FormaPago_db import insertar_forma_pago, obtener_formas_pago, actualizar_forma_pago, eliminar_forma_pago

def formapago_view(page: ft.Page):
    txt_id = ft.TextField(label="ID Forma de Pago", disabled=False)
    txt_nombre = ft.TextField(label="Nombre")

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("ID")),
            ft.DataColumn(label=ft.Text("Nombre")),
            ft.DataColumn(label=ft.Text("Editar")),
            ft.DataColumn(label=ft.Text("Eliminar")),
        ],
        rows=[]
    )

    def limpiar_formulario():
        txt_id.value = ""
        txt_nombre.value = ""
        txt_id.disabled = False
        btn_agregar.text = "Agregar"
        btn_agregar.on_click = agregar_forma_pago
        page.update()

    def cargar_datos(orden="id"):
        data_table.rows.clear()
        formas = obtener_formas_pago(orden)
        for forma in formas:
            id_fp, nombre = forma
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(id_fp))),
                        ft.DataCell(ft.Text(nombre)),
                        ft.DataCell(ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, id_fp=id_fp, n=nombre: editar_forma_pago(id_fp, n))),
                        ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id_fp=id_fp: eliminar_forma_pago_local(id_fp))),
                    ]
                )
            )
        page.update()

    def agregar_forma_pago(e):
        if txt_id.value == "" or txt_nombre.value.strip() == "":
            return
        try:
            id_val = int(txt_id.value)
            if id_val < 0:
                page.snack_bar = ft.SnackBar(ft.Text("El ID no puede ser negativo"))
                page.snack_bar.open = True
                page.update()
                return
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("El ID debe ser un número válido"))
            page.snack_bar.open = True
            page.update()
            return
        insertar_forma_pago(id_val, txt_nombre.value)
        limpiar_formulario()
        cargar_datos()

    def editar_forma_pago(id_fp, nombre):
        txt_id.value = str(id_fp)
        txt_nombre.value = nombre
        txt_id.disabled = True
        btn_agregar.text = "Actualizar"
        btn_agregar.on_click = lambda e: actualizar_forma_pago_local(id_fp)
        page.update()

    def actualizar_forma_pago_local(id_fp):
        if txt_nombre.value.strip() == "":
            page.snack_bar = ft.SnackBar(ft.Text("El nombre no puede estar vacío"))
            page.snack_bar.open = True
            page.update()
            return
        actualizar_forma_pago(id_fp, txt_nombre.value)
        limpiar_formulario()
        cargar_datos()

    def eliminar_forma_pago_local(id_fp):
        eliminar_forma_pago(id_fp)
        cargar_datos()

    btn_agregar = ft.ElevatedButton("Agregar", on_click=agregar_forma_pago)

    cargar_datos()

    return ft.View(
        "/formapago",
        controls=[
            ft.Text("Gestión de Formas de Pago", size=30, weight="bold"),
            txt_id,
            txt_nombre,
            btn_agregar,
            ft.Row([
                ft.ElevatedButton("Ordenar por ID ↑", on_click=lambda e: cargar_datos("id_asc")),
                ft.ElevatedButton("Ordenar por ID ↓", on_click=lambda e: cargar_datos("id_desc")),
                ft.ElevatedButton("Ordenar por Nombre A-Z", on_click=lambda e: cargar_datos("nombre")),
            ]),
            ft.Container(
                content=ft.Column(controls=[data_table], scroll=ft.ScrollMode.ALWAYS),
                height=300
            ),
            ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/")),
        ],
        scroll=ft.ScrollMode.AUTO
    )
