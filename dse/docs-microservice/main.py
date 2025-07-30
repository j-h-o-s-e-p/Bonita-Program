from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from domain.models import Contrato
from application.contrato_service import generar_contrato_pdf
import os

app = FastAPI()

# Crear carpeta si no existe
os.makedirs("generated", exist_ok=True)

# Servir archivos estáticos (PDFs)
app.mount("/contratos", StaticFiles(directory="generated"), name="contratos")

@app.post("/generar-contrato")
def generar_contrato(contrato: Contrato):
    archivo_pdf = generar_contrato_pdf(contrato)
    url = f"/contratos/{archivo_pdf}"
    return {
        "mensaje": "Contrato generado exitosamente",
        "url": url  # <- Esto puedes usar en Bonita
    }
