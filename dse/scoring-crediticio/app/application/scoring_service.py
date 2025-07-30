from app.domain.models import Cliente, ResultadoScoring
from fastapi import FastAPI, HTTPException
import random

def calcular_scoring(cliente: Cliente) -> ResultadoScoring:
    puntuacion = 0

    if cliente.ingresos_mensuales > 3000:
        puntuacion += 50
    elif cliente.ingresos_mensuales > 1000:
        puntuacion += 30
    else:
        puntuacion += 10

    if cliente.ocupacion.lower() in ["empleado", "profesional"]:
        puntuacion += 30
    elif cliente.ocupacion.lower() == "estudiante":
        puntuacion += 10

    aprobado = puntuacion >= 60

    return ResultadoScoring(
        puntuacion=puntuacion,
        aprobado=aprobado
    )
