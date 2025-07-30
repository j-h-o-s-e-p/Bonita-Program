from fastapi import APIRouter
from app.domain.models import Cliente, ResultadoScoring
from app.application.scoring_service import calcular_scoring
from fastapi import FastAPI, HTTPException


router = APIRouter()

app = FastAPI(title="Microservicio de Scoring Crediticio")


@app.post("/score", response_model=ResultadoScoring)
def procesar_scoring(cliente: Cliente):
    try:
        return calcular_scoring(cliente)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))