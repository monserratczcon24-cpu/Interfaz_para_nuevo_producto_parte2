#app/views/nuevo_editar.py
import flet as ft
from app.components.popup import show_popup, close_popup

#La función formulario_nuevo_editar_producto recibe on_submit,
# aquí se recibe la función para agregar o editar el producto
# (estas funciones posteriormente se crearán en mostrar_productos_httpx.py)
#initial se recibe cuando se va a editar un producto
#el valor de inital puede ser de tipo dictionary o None (sino recibe nada se asigna None)
def formulario_nuevo_editar_producto(page: ft.Page, on_submit, initial: dict | None = None):
    initial = initial or {}
    #si llega el id entonces es para editar, sino llega es nuevo registro
    titulo=ft.Text("Editar producto" if initial.get("id") else "Nuevo producto")

    # Campos
    # En el primer campo initial.get("name", "")
    # intenta recuperar de initial el valor del campo "name" sino lo encuentra regresa ""
    name = ft.TextField(label="Nombre", value=initial.get("name", ""))
    quantity = ft.TextField(label="Cantidad", value=str(initial.get("quantity", 0)))
    ingreso_date = ft.TextField(label="Ingreso (YYYY-MM-DD)", value=initial.get("ingreso_date", ""))
    min_stock = ft.TextField(label="Stock minimo", value=str(initial.get("min_stock", 0)))
    max_stock = ft.TextField(label="Stock maximo", value=str(initial.get("max_stock", 0)))

    #Botones
    btn_cancelar=ft.TextButton("Cancelar", on_click=lambda e: close())
    #al dar click en guardar se ejecuta la función save
    #run_task sirve para ejecutar funciones asincronas
    #lambda es para crear un tipo de función anonima esta función lambda recibe a la variable e
    # y esta funcion contiene a page.run_task
    btn_guardar=ft.Button("Guardar", on_click=lambda e: page.run_task(save, e))

    dlg: ft.AlertDialog # se declara la variable dlg y se espera que sea del tipo AlertDialog

    # Abre nueva ventana con el formulario
    # Modal en True bloquea la ventana y es forzoso usar algun boton para cerrar
    dlg = ft.AlertDialog(modal=False,title=titulo,content=ft.Container(width=420,
            content=ft.Column(tight=True,
                controls=[name, quantity, ingreso_date, min_stock, max_stock],
            ),
        ),
    actions=[btn_cancelar,btn_guardar],
    actions_alignment=ft.MainAxisAlignment.END,
    )

    #Función para cerrar esta ventana
    def close():
        close_popup (page)

    async def save(_e):
        # Ejemplo de Validación
        if not name.value.strip():
            await show_popup(page, "Validación", "El nombre es obligatorio.")
            return

        try:
            #recupera la información capturada en el formulario
            data = {
                "name": name.value.strip(),
                "quantity": int(quantity.value),
                "ingreso_date": ingreso_date.value.strip(),
                "min_stock": int(min_stock.value),
                "max_stock": int(max_stock.value),
            }
        except ValueError:
            await show_popup(page, "Validación", "Cantidad y stocks deben ser números enteros.")
            return

        #Se ejecuta la función que nos mandaron desde
        # la pantalla principal (Nuevo registro o editar registro)
        #Le mandamos la data capturada
        await on_submit(data)

    # Función para abrir esta ventana
    def open_():
        page. show_dialog(dlg)

    return dlg, open_, close