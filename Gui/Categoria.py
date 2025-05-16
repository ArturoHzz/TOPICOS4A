import flet as ft
from functools import partial
from Persistence.Categoria_db import obtener_categorias,insertar_categoria,eliminar_categoria_por_id,actualizar_categoria_por_id

def categoria_view(page: ft.Page):
    txt_id = ft.TextField(label="ID Categoria", disabled=False)
    txt_nombre = ft.TextField(label="Nombre")
    btn_agregar = ft.ElevatedButton("Agregar")

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
        btn_agregar.on_click = agregar_categoria
        page.update()

    def cargar_datos(orden="id"):
        data_table.rows.clear()
        categorias = obtener_categorias(orden)
        for cat in categorias:
            id_categoria, nombre = cat
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(id_categoria))),
                        ft.DataCell(ft.Text(nombre)),
                        ft.DataCell(
                            ft.IconButton(icon=ft.icons.EDIT, on_click=partial(editar_categoria, id_categoria, nombre))
                        ),
                        ft.DataCell(
                            ft.IconButton(icon=ft.icons.DELETE, on_click=partial(eliminar_categoria, id_categoria))
                        ),
                    ]
                )
            )
        page.update()

    def agregar_categoria(e):
        if txt_id.value == "" or txt_nombre.value == "":
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
        insertar_categoria(id_val, txt_nombre.value)
        limpiar_formulario()
        cargar_datos()

    def editar_categoria(id_categoria, nombre_actual, e=None):
        txt_id.value = str(id_categoria)
        txt_nombre.value = nombre_actual
        txt_id.disabled = True
        btn_agregar.text = "Actualizar"
        btn_agregar.on_click = lambda e: actualizar_categoria(id_categoria)
        page.update()

    def actualizar_categoria(id_categoria):
        if txt_nombre.value.strip() == "":
            page.snack_bar = ft.SnackBar(ft.Text("El nombre no puede estar vacío"))
            page.snack_bar.open = True
            page.update()
            return
        actualizar_categoria_por_id(id_categoria, txt_nombre.value)
        limpiar_formulario()
        cargar_datos()

    def eliminar_categoria(id_categoria, e=None):
        eliminar_categoria_por_id(id_categoria)
        cargar_datos()

    cargar_datos()

    return ft.View(
    "/categoria",
    controls=[
        ft.Text("Gestión de Categorías", size=30, weight="bold"),
        txt_id,
        txt_nombre,
        btn_agregar,
        ft.Row([
            ft.ElevatedButton("Ordenar por ID ↑", on_click=lambda e: cargar_datos("id_asc")),
            ft.ElevatedButton("Ordenar por ID ↓", on_click=lambda e: cargar_datos("id_desc")),
            ft.ElevatedButton("Ordenar por Nombre A-Z", on_click=lambda e: cargar_datos("nombre")),
        ]),
        ft.Container(
            content=ft.Column(
                controls=[data_table],
                scroll=ft.ScrollMode.ALWAYS
            ),
            height=300
        ),
        ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/")),
    ],
    scroll=ft.ScrollMode.AUTO
)


