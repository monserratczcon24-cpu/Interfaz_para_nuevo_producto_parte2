import requests
from typing import Dict, Any

BASE_URL = "http://localhost:8000"


# LISTAR PRODUCTOS desde FastAPI
# GET /products/?limit=500&offset=0
# Retorna: {"total": X, "items": [...]}
def list_products(limit: int = 500, offset: int = 0) -> Dict[str, Any]:
    response = requests.get(
        f"{BASE_URL}/products/",
        params={"limit": limit, "offset": offset}
    )
    response.raise_for_status()
    return response.json()


# OBTENER PRODUCTO POR ID
# GET /products/{product_id}
def get_product(product_id: str) -> Dict | None:
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


# CREAR PRODUCTO
# POST /products/
def create_product(producto: Dict) -> Dict:
    response = requests.post(f"{BASE_URL}/products/", json=producto)
    response.raise_for_status()
    return response.json()


# ACTUALIZAR PRODUCTO
# PUT /products/{product_id}
def update_product(product_id: str, datos: Dict) -> Dict | None:
    response = requests.put(f"{BASE_URL}/products/{product_id}", json=datos)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


# ELIMINAR PRODUCTO
# DELETE /products/{product_id}
def delete_product(product_id: str) -> bool:
    response = requests.delete(f"{BASE_URL}/products/{product_id}")
    if response.status_code == 404:
        return False
    response.raise_for_status()
    return True