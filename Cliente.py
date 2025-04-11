import flet as ft

def cliente(page: ft.Page):
    page.title = "Cliente"

    # Campos de entrada
    nombre_input = ft.TextField(label="Nombres", width=300)
    apellido_input = ft.TextField(label="Apellidos", width=300)
    telefono_input = ft.TextField(label="Telefono", width=300)
    correo_input = ft.TextField(label="Correo", width=300)
    resultado_texto = ft.Text("")
    # Botón para enviar
    def enviar_click(e):
        resultado_texto.value = f"Nombres: {nombre_input.value} | Apellidos: {apellido_input.value}"
        page.update()

    boton_enviar = ft.ElevatedButton("Enviar", on_click=enviar_click)

    # Agregamos al layout
    page.add(
        ft.Column(
            [
                ft.Text("Añadir Cliente", size=25, weight="bold"),
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

ft.app(target=cliente)






