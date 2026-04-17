import flet as ft
from typing import Any

from app.services.transacciones_api_productos import (
    list_products,
    get_product,
    create_product,
    update_product,
    delete_product,
)

from app.components.popup import (
    show_popup,
    show_popup_auto_close,
    show_snackbar,
    confirm_dialog,
)

from app.components.error import ApiError, api_error_to_text
from app.styles.estilos import Colors, Textos_estilos, Card

from app.views.nuevo_editar import formulario_nuevo_editar_producto


def products_view(page: ft.Page) -> ft.Control:

    def inicio_nuevo_producto(e):

        async def crear_nuevo_producto(data: dict):
            try:
                await create_product(data)
                await show_snackbar(page, "Éxito", "Producto creado.", bgcolor=Colors.SUCCESS)
                await actualizar_data()

            except ApiError as ex:
                await show_popup(page, "Error", api_error_to_text(ex))

            except Exception as ex:
                await show_snackbar(page, "Error", str(ex), bgcolor=Colors.DANGER)

        dlg, open_, close = formulario_nuevo_editar_producto(
            page,
            on_submit=crear_nuevo_producto,
            initial=None
        )

        open_()


    btn_nuevo = ft.Button(
        "Nuevo producto",
        icon=ft.Icons.ADD,
        on_click=inicio_nuevo_producto
    )

    rows_data: list[dict[str, Any]] = []
    total_items = 0

    total_text = ft.Text(
        "Total de productos: (cargando...)",
        style=Textos_estilos.H4
    )

    
    columnas = [
        ft.DataColumn(label=ft.Text("Nombre", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Cantidad", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Ingreso", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Min", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Max", style=Textos_estilos.H4)),
    ]

    data = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("cargando...")),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
            ]
        )
    ]

    tabla = ft.DataTable(
        columns=columnas,
        rows=data,
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48,
    )

    async def actualizar_data():
        nonlocal rows_data, total_items
        try:
            data = list_products(limit=500, offset=0)

            total_items = int(data.get("total", 0))
            total_text.value = "Total de productos: " + str(total_items)

            rows_data = data.get("items", []) or []

            actualizar_filas()

        except Exception as ex:
            await show_snackbar(page, "Error", str(ex), bgcolor=Colors.DANGER)

    def actualizar_filas():
        nuevas_filas = []
        for p in rows_data:
            nuevas_filas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(p.get("name", ""))),
                        ft.DataCell(ft.Text(str(p.get("quantity", "")))),
                        ft.DataCell(ft.Text(p.get("ingreso_date", "") or "")),
                        ft.DataCell(ft.Text(str(p.get("min_stock", "")))),
                        ft.DataCell(ft.Text(str(p.get("max_stock", "")))),
                    ]
                )
            )

        tabla.rows = nuevas_filas
        page.update()

    page.run_task(actualizar_data)

    contenido = ft.Column(
        expand=True,
        spacing=30,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            btn_nuevo,
            total_text,
            ft.Container(content=tabla)
        ]
    )

    tarjeta = ft.Container(
        content=contenido,
        **Card.tarjeta
    )

    return tarjeta