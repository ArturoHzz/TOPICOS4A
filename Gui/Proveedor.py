import flet as ft
from Persistence.Proveedor_db import insertar_proveedor, obtener_proveedores, actualizar_proveedor, eliminar_proveedor

def proveedor_view(page: ft.Page):
    txt_id = ft.TextField(label="ID Proveedor", disabled=False)
    txt_nombre = ft.TextField(label="Nombre")
    txt_telefono = ft.TextField(label="Teléfono")
    txt_email = ft.TextField(label="Email")
    txt_direccion = ft.TextField(label="Dirección")
    txt_rfc = ft.TextField(label="RFC")

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("ID")),
            ft.DataColumn(label=ft.Text("Nombre")),
            ft.DataColumn(label=ft.Text("Teléfono")),
            ft.DataColumn(label=ft.Text("Email")),
            ft.DataColumn(label=ft.Text("Dirección")),
            ft.DataColumn(label=ft.Text("RFC")),
            ft.DataColumn(label=ft.Text("Editar")),
            ft.DataColumn(label=ft.Text("Eliminar")),
        ],
        rows=[]
    )

    def limpiar_formulario():
        txt_id.value = ""
        txt_nombre.value = ""
        txt_telefono.value = ""
        txt_email.value = ""
        txt_direccion.value = ""
        txt_rfc.value = ""
        txt_id.disabled = False
        btn_agregar.text = "Agregar"
        btn_agregar.on_click = agregar_proveedor
        page.update()

    def cargar_datos(orden="id"):
        data_table.rows.clear()
        proveedores = obtener_proveedores(orden)
        for prov in proveedores:
            idp, nom, tel, email, dir, rfc = prov
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(idp))),
                        ft.DataCell(ft.Text(nom)),
                        ft.DataCell(ft.Text(tel)),
                        ft.DataCell(ft.Text(email)),
                        ft.DataCell(ft.Text(dir)),
                        ft.DataCell(ft.Text(rfc)),
                        ft.DataCell(ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, idp=idp, n=nom, t=tel, em=email, d=dir, r=rfc: editar_proveedor(idp, n, t, em, d, r))),
                        ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, idp=idp: eliminar_proveedor_local(idp))),
                    ]
                )
            )
        page.update()

    def agregar_proveedor(e):
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

        insertar_proveedor(id_val, txt_nombre.value, txt_telefono.value, txt_email.value, txt_direccion.value, txt_rfc.value)
        limpiar_formulario()
        cargar_datos()

    def editar_proveedor(idp, nombre, telefono, email, direccion, rfc):
        txt_id.value = str(idp)
        txt_nombre.value = nombre
        txt_telefono.value = telefono
        txt_email.value = email
        txt_direccion.value = direccion
        txt_rfc.value = rfc
        txt_id.disabled = True
        btn_agregar.text = "Actualizar"
        btn_agregar.on_click = lambda e: actualizar_proveedor_local(idp)
        page.update()

    def actualizar_proveedor_local(idp):
        if txt_nombre.value.strip() == "":
            page.snack_bar = ft.SnackBar(ft.Text("El nombre no puede estar vacío"))
            page.snack_bar.open = True
            page.update()
            return
        actualizar_proveedor(idp, txt_nombre.value, txt_telefono.value, txt_email.value, txt_direccion.value, txt_rfc.value)
        limpiar_formulario()
        cargar_datos()

    def eliminar_proveedor_local(idp):
        eliminar_proveedor(idp)
        cargar_datos()

    btn_agregar = ft.ElevatedButton("Agregar", on_click=agregar_proveedor)

    cargar_datos()

    return ft.View(
        "/proveedor",
        controls=[
            ft.Text("Gestión de Proveedores", size=30, weight="bold"),
            txt_id,
            txt_nombre,
            txt_telefono,
            txt_email,
            txt_direccion,
            txt_rfc,
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
