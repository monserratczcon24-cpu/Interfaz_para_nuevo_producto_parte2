import flet as ft

class Colors:
    BG = "#e6e8ee"
    SURFACE = "#111827"
    CARD = "#0f172a"
    BORDER = "#243041"
    TEXT = "#3F4041"
    SOMBRA = "#636b76"
    PRIMARY = "#3b82f6"
    SUCCESS = "#18AE7E"
    INFO = "#0dcaf0"
    WARNING = "#f59e0b"
    DANGER = "#ef4444"
    HIGHLIGHT = "#fde68a"
    WHITE = "#FFFFFF"
    BLACK = "#000000"

class Textos_estilos:
    H1=ft.TextStyle(size=48, height=1.2, weight=ft.FontWeight.W_300, font_family="sans-serif", color=Colors.TEXT)
    H2=ft.TextStyle(size=40, height=1.2, weight=ft.FontWeight.W_300, font_family="sans-serif", color=Colors.TEXT)
    H3=ft.TextStyle(size=32, height=1.2, weight=ft.FontWeight.W_300, font_family="sans-serif", color=Colors.TEXT)
    H4=ft.TextStyle(size=26, height=1.2, weight=ft.FontWeight.W_300, font_family="sans-serif", color=Colors.TEXT)
    H5=ft.TextStyle(size=18, height=1.2, weight=ft.FontWeight.W_300, font_family="sans-serif", color=Colors.TEXT)

class Inputs:
    INPUT_PRIMARY = {
        "border_color": Colors.BORDER,
        "focused_border_color": Colors.PRIMARY,
        "cursor_color": Colors.PRIMARY,
        "width": 500,
        "text_style": ft.TextStyle(size=18, color=Colors.TEXT),
        "label_style": Textos_estilos.H5,
        "hint_style": Textos_estilos.H5,
        "bgcolor": Colors.BG
    }

class Buttons:
    BUTTON_PRIMARY = ft.ButtonStyle(bgcolor=Colors.PRIMARY, color=Colors.TEXT, padding=10, shape=ft.RoundedRectangleBorder(radius=8))
    BUTTON_SUCCESS = ft.ButtonStyle(bgcolor=Colors.SUCCESS, color=Colors.TEXT, padding=10, shape=ft.RoundedRectangleBorder(radius=8))
    BUTTON_DANGER = ft.ButtonStyle(bgcolor=Colors.DANGER, color=Colors.TEXT, padding=10, shape=ft.RoundedRectangleBorder(radius=8))

class Card:
    tarjeta = {
        "width": 900,
        "padding": 16,
        "border_radius": 12,
        "bgcolor": Colors.BG,
        "border": ft.Border.all(2, Colors.BORDER)
    }