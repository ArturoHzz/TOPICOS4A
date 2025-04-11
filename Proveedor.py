import flet as ft
def proveedor(page: ft.Page):
    page.title = "Proveedor"

    # Campos de entrada
    nombre_input = ft.TextField(label="Nombres", width=300)
    apellido_input = ft.TextField(label="Apellidos", width=300)
    correo_input = ft.TextField(label="Correo", width=300)
    telefono_input = ft.TextField(label="Telefono", width=300)
    direccion_input = ft.TextField(label="Direccion", width=300)
    # Botón para enviar
    def enviar_click(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Datos recibidos"),
            content=ft.Text(f"Nombre: {nombre_input.value}\nApellido: {apellido_input.value}"),
        )
        page.dialog.open = True
        page.update()

    boton_enviar = ft.ElevatedButton("Enviar", on_click=enviar_click)

    # Agregamos al layout
    page.add(
        ft.Column(
            [
                ft.Text("Añadir Proveedor", size=25, weight="bold"),
                nombre_input,
                apellido_input,
                correo_input,
                telefono_input,
                direccion_input,
                boton_enviar,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
    )

ft.app(target=proveedor)