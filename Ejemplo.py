import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Selector de fecha"
    page.scroll = ft.ScrollMode.AUTO

    selected_date_text = ft.Text()

    # Crear el DatePicker con evento de cambio
    date_picker = ft.DatePicker(
        on_change=lambda e: mostrar_fecha(e.data),
        first_date=datetime.date(2020, 1, 1),
        last_date=datetime.date(2035, 12, 31)
    )
    page.overlay.append(date_picker)

    def mostrar_fecha(fecha_str):
        selected_date_text.value = f"Fecha seleccionada: {fecha_str}"
        page.update()

    # Botón para abrir el DatePicker
    btn_abrir = ft.ElevatedButton(
        text="Seleccionar Fecha",
        on_click=lambda _: abrir_date_picker()
    )

    def abrir_date_picker():
        date_picker.open = True
        page.update()

    page.add(btn_abrir, selected_date_text)

ft.app(target=main)



