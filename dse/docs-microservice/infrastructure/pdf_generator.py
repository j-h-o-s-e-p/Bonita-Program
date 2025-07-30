from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from domain.models import Contrato

def crear_contrato_pdf(nombre_archivo: str, contrato: Contrato):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont("Helvetica", 20)
    c.drawString(100, 750, "CONTRATO CREDITICIO")
    c.line(100, 745, 500, 745)

    c.setFont("Helvetica", 14)
    c.drawString(100, 720, "Entre:")
    c.drawString(100, 700, f"Parte A: {contrato.parte_a}")
    c.drawString(100, 680, f"DNI Parte A: {contrato.dni}")
    c.drawString(100, 660, f"Parte B: Banco de Credito del Peru BCP")

    y = 630
    for parrafo in contrato.contenido:
        c.drawString(100, y, parrafo)
        y -= 20

    c.drawString(100, 200, "Firma Parte A: _________________________")
    c.drawString(100, 180, "Firma Parte B: _________________________")
    c.drawString(100, 160, f"Fecha: {contrato.fecha}")
    c.save()
