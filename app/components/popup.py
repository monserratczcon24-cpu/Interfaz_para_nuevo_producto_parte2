import flet as ft
from app.styles.estilos import Colors,Buttons
import asyncio

async def show_popup(page: ft.Page, title: str, message: str, bgcolor:str=Colors.DANGER, txtcolor:str=Colors.WHITE):
    dlg = ft.AlertDialog(
        title_padding=0, 
        content_padding=0,
        title=ft.Container(
            bgcolor=bgcolor,
            padding=12,
            border_radius=ft.BorderRadius(18, 18, 0, 0),
            content=ft.Text(title,color=txtcolor,weight=ft.FontWeight.BOLD)
        ),
        content=ft.Container(
            padding=10,
            content=ft.Text(message),
        ),
        actions=[ft.Button("OK", on_click=lambda e: close_popup(page), style=Buttons.BUTTON_PRIMARY)]
    )
    page.show_dialog(dlg)


def close_popup(page: ft.Page):
    pop = getattr(page, "pop_dialog", None)
    if callable(pop):
        page.pop_dialog()
    page.update()

async def show_popup_auto_close(page: ft.Page,title: str,message: str, bgcolor:str=Colors.DANGER, txtcolor:str=Colors.WHITE, seconds: int = 3):
    dlg = ft.AlertDialog(
        title_padding=0, 
        content_padding=0,
        title=ft.Container(
            bgcolor=bgcolor,
            padding=12,
            border_radius=ft.BorderRadius(18, 18, 0, 0),
            content=ft.Text(title,color=txtcolor,weight=ft.FontWeight.BOLD)
        ),
        content=ft.Container(
            padding=10,
            content=ft.Text(message),
        )
    )    
    # Mostrar popup
    page.show_dialog(dlg)

    # Esperar N segundos (sin bloquear UI)
    await asyncio.sleep(seconds)

    # Cerrar popup si sigue abierto
    pop = getattr(page, "pop_dialog", None)
    if callable(pop):
        pop()

    page.update()

async def show_snackbar(page: ft.Page,title:str,message: str, bgcolor: str=Colors.DANGER, txtcolor:str=Colors.WHITE, seconds: int = 3) -> None:
    sb = ft.SnackBar(
        content=ft.Text(message, color=txtcolor),
        bgcolor=bgcolor,
        duration=ft.Duration(seconds=seconds),
    )
    page.show_dialog(sb)

async def confirm_dialog(page: ft.Page, title:str, message:str, function_on_yes, bgcolor:str=Colors.DANGER, txtcolor:str=Colors.WHITE):
    dlg = ft.AlertDialog(
        modal=True,
        title_padding=0,
        content_padding=0,
        title=ft.Container(bgcolor=bgcolor,padding=12,border_radius=ft.BorderRadius(18,18,0,0),content=ft.Text(title,color=txtcolor, weight=ft.FontWeight.BOLD)), 
        content=ft.Container(padding=10,content=ft.Text(message)), 
        actions=[ft.TextButton("Cancelar",on_click=lambda e: _close_confirm_dialog(page)),
                 ft.Button("Si, borrar", on_click=lambda e: _yes(page, function_on_yes))], 
                 actions_alignment=ft.MainAxisAlignment.END
    )
    page.show_dialog(dlg)

def _close_confirm_dialog(page: ft.Page):
    pop = getattr(page,"pop_dialog",None)
    if callable(pop):
        page.pop_dialog()
    page.update()

def _yes(page:ft.Page, function_on_yes):
    pop = getattr(page,"pop_dialog",None)
    if callable(pop):
        page.pop_dialog()
    page.update()
    function_on_yes()