import flet as ft
def categorias(page: ft.Page):
    page.title = "Categorias"

    # Campos de entrada
    nombre_input = ft.TextField(label="Nombre", width=300)
    descripcion_input = ft.TextField(label="Descripcion",width=300)
    # Botón para enviar
    def enviar_click(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Datos recibidos"),
            content=ft.Text(f"Nombre: {nombre_input.value}\nApellido: {descripcion_input.value}"),
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
                descripcion_input,
                boton_enviar,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
    )

ft.app(target=categorias)