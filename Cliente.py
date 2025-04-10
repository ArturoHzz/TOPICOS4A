import flet as ft

def ventana(page: ft.Page):
    page.title = "Añadir Cliente"

    # Campos de entrada
    nombre_input = ft.TextField(label="Nombre", width=300)
    apellido_input = ft.TextField(label="Apellido", width=300)
    telefono_input = ft.TextField(label="Telefono", width=300)
    correo_input = ft.TextField(label="Correo", width=300)

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
                ft.Text("Formulario de Cliente", size=25, weight="bold"),
                nombre_input,
                apellido_input,
                telefono_input,
                correo_input,
                boton_enviar,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
    )

ft.app(target=ventana)



