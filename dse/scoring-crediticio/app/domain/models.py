from pydantic import BaseModel
from typing import Literal

class Cliente(BaseModel):
    dni: str
    nombre: str
    ocupacion: Literal["empleado", "profesional", "estudiante"]
    ingresos_mensuales: float

class ResultadoScoring(BaseModel):
    puntuacion: int
    aprobado: bool
