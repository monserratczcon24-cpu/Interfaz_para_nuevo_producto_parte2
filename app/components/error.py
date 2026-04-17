from __future__ import annotations
from typing import Any


class ApiError(Exception):
    """
    Excepción estándar para errores al consumir la API.
    - message: texto base del error
    - status_code: código HTTP (int). Usa 0 para errores de red/conexión.
    - payload: dict opcional con detalle estructurado devuelto por la API
    """
    def __init__(self, message: str, status_code: int, payload: Any = None):
        super().__init__(message)
        self.status_code = status_code  # <-- sin coma
        self.payload = payload or {}


def api_error_to_text(ex: ApiError) -> str:
    """
    Convierte ApiError a un texto amigable para UI (SnackBar/Toast/Dialog).
    Soporta payloads tipo:
      - {"error": "...", "detalles": [...]}
      - {"detail": "..."}
      - {"error": "..."}
    """
    payload = getattr(ex, "payload", None) or {}

    if isinstance(payload, dict):
        detalles = payload.get("detalles")
        if isinstance(detalles, list) and detalles:
            return "\n".join(str(x) for x in detalles)

        if "detail" in payload:
            return str(payload["detail"])
        if "error" in payload:
            return str(payload["error"])

    return str(ex)