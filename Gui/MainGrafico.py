import flet as ft
from Gui.Categoria import categoria_view
from Gui.Cliente import cliente_view
from Gui.Empleado import empleado_view
from Gui.FormaPago import formapago_view
from Gui.Proveedor import proveedor_view
from Gui.Unidad import unidad_view

def main(page: ft.Page):
    page.title = "Sistema Farmacia"

    def on_window_event(e):
        if e.data == "close":
            print("Aplicación cerrada por el usuario")
            page.window_destroy()

    page.on_window_event = on_window_event

    def route_change(e):
        page.views.clear()

        if page.route == "/categoria":
            page.views.append(categoria_view(page))
        elif page.route == "/cliente":
            page.views.append(cliente_view(page))
        elif page.route == "/empleado":
            page.views.append(empleado_view(page))
        elif page.route == "/formapago":
            page.views.append(formapago_view(page))
        elif page.route == "/proveedor":
            page.views.append(proveedor_view(page))
        elif page.route == "/unidad":
            page.views.append(unidad_view(page))
        else:
            # Vista principal estilizada
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("Menú Principal", size=35, weight="bold", text_align=ft.TextAlign.CENTER),
                                    ft.ElevatedButton("Categoría", icon=ft.icons.CATEGORY, on_click=lambda e: page.go("/categoria")),
                                    ft.ElevatedButton("Cliente", icon=ft.icons.PERSON, on_click=lambda e: page.go("/cliente")),
                                    ft.ElevatedButton("Empleado", icon=ft.icons.BADGE, on_click=lambda e: page.go("/empleado")),
                                    ft.ElevatedButton("Forma de Pago", icon=ft.icons.PAYMENTS, on_click=lambda e: page.go("/formapago")),
                                    ft.ElevatedButton("Proveedor", icon=ft.icons.LOCAL_SHIPPING, on_click=lambda e: page.go("/proveedor")),
                                    ft.ElevatedButton("Unidad", icon=ft.icons.SQUARE_FOOT, on_click=lambda e: page.go("/unidad")),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=15
                            ),
                            padding=40,
                            alignment=ft.alignment.center
                        )
                    ],
                    scroll=ft.ScrollMode.AUTO
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)
