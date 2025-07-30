from pydantic import BaseModel
from typing import List

class Contrato(BaseModel):
    parte_a: str
    dni: str
    parte_b: str
    fecha: str
    contenido: List[str]
