import flet as ft
from Persistence.Unidad_db import insertar_unidad, obtener_unidades, actualizar_unidad, eliminar_unidad

def unidad_view(page: ft.Page):
    txt_id = ft.TextField(label="ID Unidad", disabled=False)
    txt_nombre = ft.TextField(label="Nombre")
    txt_abreviatura = ft.TextField(label="Abreviatura")

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("ID")),
            ft.DataColumn(label=ft.Text("Nombre")),
            ft.DataColumn(label=ft.Text("Abreviatura")),
            ft.DataColumn(label=ft.Text("Editar")),
            ft.DataColumn(label=ft.Text("Eliminar")),
        ],
        rows=[]
    )

    def limpiar_formulario():
        txt_id.value = ""
        txt_nombre.value = ""
        txt_abreviatura.value = ""
        txt_id.disabled = False
        btn_agregar.text = "Agregar"
        btn_agregar.on_click = agregar_unidad
        page.update()

    def cargar_datos(orden="id"):
        data_table.rows.clear()
        unidades = obtener_unidades(orden)
        for u in unidades:
            idu, nombre, abrev = u
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(idu))),
                        ft.DataCell(ft.Text(nombre)),
                        ft.DataCell(ft.Text(abrev)),
                        ft.DataCell(ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, idu=idu, n=nombre, a=abrev: editar_unidad(idu, n, a))),
                        ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, idu=idu: eliminar_unidad_local(idu))),
                    ]
                )
            )
        page.update()

    def agregar_unidad(e):
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
        insertar_unidad(id_val, txt_nombre.value, txt_abreviatura.value)
        limpiar_formulario()
        cargar_datos()

    def editar_unidad(idu, nombre, abrev):
        txt_id.value = str(idu)
        txt_nombre.value = nombre
        txt_abreviatura.value = abrev
        txt_id.disabled = True
        btn_agregar.text = "Actualizar"
        btn_agregar.on_click = lambda e: actualizar_unidad_local(idu)
        page.update()

    def actualizar_unidad_local(idu):
        if txt_nombre.value.strip() == "":
            page.snack_bar = ft.SnackBar(ft.Text("El nombre no puede estar vacío"))
            page.snack_bar.open = True
            page.update()
            return
        actualizar_unidad(idu, txt_nombre.value, txt_abreviatura.value)
        limpiar_formulario()
        cargar_datos()

    def eliminar_unidad_local(idu):
        eliminar_unidad(idu)
        cargar_datos()

    btn_agregar = ft.ElevatedButton("Agregar", on_click=agregar_unidad)

    cargar_datos()

    return ft.View(
        "/unidad",
        controls=[
            ft.Text("Gestión de Unidades", size=30, weight="bold"),
            txt_id,
            txt_nombre,
            txt_abreviatura,
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
