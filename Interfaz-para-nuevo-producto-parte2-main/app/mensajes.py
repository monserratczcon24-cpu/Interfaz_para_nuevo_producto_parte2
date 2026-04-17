import flet as ft
from app. styles.estilos import Buttons, Card, Colors, Inputs, Textos_estilos
from app. components.popup import show_popup, show_popup_auto_close, show_snackbar

def main(page: ft.Page):
    title = ft.Text("Mi app Flet", style=Textos_estilos.H4, text_align=ft. TextAlign. CENTER)
    subtitle = ft.Text("Sistema de estilos centralizado", style=Textos_estilos.H5)
    name = ft.TextField (label="Nombre", ** Inputs. INPUT_PRIMARY)

    async def on_click(e):
        titulo="Saludo"
        mensaje=f"Hola {name.value}" 

    btn = ft.Button("Saludar", on_click=on_click, style=Buttons.BUTTON_PRIMARY)

    page.add(title, subtitle, name, btn)

if __name__ == "__main__":
    ft.run (main)