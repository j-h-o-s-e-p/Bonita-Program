from domain.models import Contrato
from infrastructure.pdf_generator import crear_contrato_pdf
import uuid

from infrastructure.pdf_generator import crear_contrato_pdf
from domain.models import Contrato

def generar_contrato_pdf(contrato: Contrato) -> str:
    nombre_archivo = f"contrato_{contrato.dni}.pdf"
    ruta_completa = f"generated/{nombre_archivo}"
    crear_contrato_pdf(ruta_completa, contrato)
    return nombre_archivo

