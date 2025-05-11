import flet as ft
def formaPago(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.title = "Forma de pago"

    # Campos de entrada
    nombre_input = ft.TextField(
        label="Nombre", 
        width=300,
        bgcolor = ft.colors.PINK,
        label_style = ft.TextStyle(color=ft.colors.BLACK)
        )
    #Estilos de botones
    boton_enviar = ft.ElevatedButton(
        text ="Enviar",
        style = ft.ButtonStyle(
            bgcolor = ft.colors.GREEN,
            color = ft.colors.BLACK,
            padding = 13,
            shape = ft.RoundedRectangleBorder(radius=10),
            text_style = ft.TextStyle(
            size = 18,
            weight = ft.FontWeight.BOLD,
        )
        )
    )
    boton_salir = ft.ElevatedButton(
        text ="Salir",
        style = ft.ButtonStyle(
            bgcolor = ft.colors.RED,
            color = ft.colors.BLACK,
            padding = 13,
            shape = ft.RoundedRectangleBorder(radius=10),
            text_style = ft.TextStyle(
            size = 18,
            weight = ft.FontWeight.BOLD,
        )
        )
    )
    fila_botones = ft.Row(
        controls = [boton_enviar, boton_salir],
        alignment = ft.MainAxisAlignment.CENTER  # Para alinearlos a la derecha
    ) 

    # Columna centrada con los campos
    contenido = ft.Column(
        [
            ft.Text("Añadir Forma de pago", size=30, weight="bold", color=ft.colors.WHITE),
            nombre_input,
            fila_botones
        ],
        alignment = ft.MainAxisAlignment.CENTER,  
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,  
    )

    # Contenedor que ocupa toda la pantalla y centra la columna
    page.add(
        ft.Container(
            content = contenido,
            alignment = ft.alignment.center,
            expand=True  # Ocupa todo el espacio de la pantalla
        )
    )

ft.app(target = formaPago)