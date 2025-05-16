import flet as ft
from Persistence.Empleado_db import insertar_empleado, obtener_empleados, actualizar_empleado_id, eliminar_empleado_id

def empleado_view(page: ft.Page):
    txt_id = ft.TextField(label="ID Empleado", disabled=False)
    txt_nombre = ft.TextField(label="Nombres")
    txt_apellidos = ft.TextField(label="Apellidos")
    txt_rfc = ft.TextField(label="RFC")

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("ID")),
            ft.DataColumn(label=ft.Text("Nombres")),
            ft.DataColumn(label=ft.Text("Apellidos")),
            ft.DataColumn(label=ft.Text("RFC")),
            ft.DataColumn(label=ft.Text("Editar")),
            ft.DataColumn(label=ft.Text("Eliminar")),
        ],
        rows=[]
    )

    def limpiar_formulario():
        txt_id.value = ""
        txt_nombre.value = ""
        txt_apellidos.value = ""
        txt_rfc.value = ""
        txt_id.disabled = False
        btn_agregar.text = "Agregar"
        btn_agregar.on_click = agregar_empleado
        page.update()

    def cargar_datos(orden="id"):
        data_table.rows.clear()
        empleados = obtener_empleados(orden)
        for emp in empleados:
            id_emp, nombres, apellidos, rfc = emp
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(id_emp))),
                        ft.DataCell(ft.Text(nombres)),
                        ft.DataCell(ft.Text(apellidos)),
                        ft.DataCell(ft.Text(rfc)),
                        ft.DataCell(ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, id_emp=id_emp, n=nombres, a=apellidos, r=rfc: editar_empleado(id_emp, n, a, r))),
                        ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id_emp=id_emp: eliminar_empleado(id_emp))),
                    ]
                )
            )
        page.update()

    def agregar_empleado(e):
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

        insertar_empleado(id_val, txt_nombre.value, txt_apellidos.value, txt_rfc.value)
        limpiar_formulario()
        cargar_datos()

    def editar_empleado(id_emp, nombres, apellidos, rfc):
        txt_id.value = str(id_emp)
        txt_nombre.value = nombres
        txt_apellidos.value = apellidos
        txt_rfc.value = rfc
        txt_id.disabled = True
        btn_agregar.text = "Actualizar"
        btn_agregar.on_click = lambda e: actualizar_empleado(id_emp)
        page.update()

    def actualizar_empleado(id_emp):
        if txt_nombre.value.strip() == "":
            page.snack_bar = ft.SnackBar(ft.Text("El nombre no puede estar vacío"))
            page.snack_bar.open = True
            page.update()
            return
        actualizar_empleado_id(id_emp, txt_nombre.value, txt_apellidos.value, txt_rfc.value)
        limpiar_formulario()
        cargar_datos()

    def eliminar_empleado(id_emp):
        eliminar_empleado_id(id_emp)
        cargar_datos()

    btn_agregar = ft.ElevatedButton("Agregar", on_click=agregar_empleado)

    cargar_datos()

    return ft.View(
        "/empleado",
        controls=[
            ft.Text("Gestión de Empleados", size=30, weight="bold"),
            txt_id,
            txt_nombre,
            txt_apellidos,
            txt_rfc,
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
