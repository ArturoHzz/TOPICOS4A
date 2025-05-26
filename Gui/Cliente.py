import flet as ft
from Persistence.Cliente_db import insertar_cliente, obtener_cliente, actualizar_cliente_id, eliminar_cliente_id

def cliente_view(page: ft.Page):
    txt_id = ft.TextField(label="ID Teléfono(10 Digitos)", disabled=False,max_length=10)
    txt_nombre = ft.TextField(label="Nombres")
    txt_apellidos = ft.TextField(label="Apellidos")
    txt_correo = ft.TextField(label="Correo")

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("ID")),
            ft.DataColumn(label=ft.Text("Nombres")),
            ft.DataColumn(label=ft.Text("Apellidos")),
            ft.DataColumn(label=ft.Text("Correo")),
            ft.DataColumn(label=ft.Text("Editar")),
            ft.DataColumn(label=ft.Text("Eliminar")),
        ],
        rows=[]
    )

    def limpiar_formulario():
        txt_id.value = ""
        txt_nombre.value = ""
        txt_apellidos.value = ""
        txt_correo.value = ""
        txt_id.disabled = False
        btn_agregar.text = "Agregar"
        btn_agregar.on_click = agregar_cliente
        page.update()

    def cargar_datos(orden="id"):
        data_table.rows.clear()
        clientes = obtener_cliente(orden)
        for cliente in clientes:
            id_tel, nombres, apellidos, correo = cliente
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(id_tel))),
                        ft.DataCell(ft.Text(nombres)),
                        ft.DataCell(ft.Text(apellidos)),
                        ft.DataCell(ft.Text(correo)),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.icons.EDIT,
                                on_click=lambda e, id_tel=id_tel, n=nombres, a=apellidos, c=correo:
                                editar_cliente(id_tel, n, a, c)
                            )
                        ),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                on_click=lambda e, id_tel=id_tel: eliminar_cliente(id_tel)
                            )
                        ),
                    ]
                )
            )
        page.update()

    def agregar_cliente(e):
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

        insertar_cliente(id_val, txt_nombre.value, txt_apellidos.value, txt_correo.value)
        limpiar_formulario()
        cargar_datos()

    def editar_cliente(id_tel, nombres, apellidos, correo):
        txt_id.value = str(id_tel)
        txt_nombre.value = nombres
        txt_apellidos.value = apellidos
        txt_correo.value = correo
        txt_id.disabled = True
        btn_agregar.text = "Actualizar"
        btn_agregar.on_click = lambda e: actualizar_cliente(id_tel)
        page.update()

    def actualizar_cliente(id_tel):
        if txt_nombre.value.strip() == "":
            page.snack_bar = ft.SnackBar(ft.Text("El nombre no puede estar vacío"))
            page.snack_bar.open = True
            page.update()
            return
        actualizar_cliente_id(id_tel, txt_nombre.value, txt_apellidos.value, txt_correo.value)
        limpiar_formulario()
        cargar_datos()

    def eliminar_cliente(id_tel):
        eliminar_cliente_id(id_tel)
        cargar_datos()

    btn_agregar = ft.ElevatedButton("Agregar", on_click=agregar_cliente)

    cargar_datos()

    return ft.View(
        "/cliente",
        controls=[
            ft.Text("Gestión de Clientes", size=30, weight="bold"),
            txt_id,
            txt_nombre,
            txt_apellidos,
            txt_correo,
            btn_agregar,
            ft.Row([
                ft.ElevatedButton("Ordenar por ID ↑", on_click=lambda e: cargar_datos("id_asc")),
                ft.ElevatedButton("Ordenar por ID ↓", on_click=lambda e: cargar_datos("id_desc")),
                ft.ElevatedButton("Ordenar por Apellido A-Z", on_click=lambda e: cargar_datos("apellido")),
            ]),
            ft.Container(
                content=ft.Column(controls=[data_table], scroll=ft.ScrollMode.ALWAYS),
                height=300
            ),
            ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/")),
        ],
        scroll=ft.ScrollMode.AUTO
    )





