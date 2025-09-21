from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Dia(BaseModel):
    valor: float
    quantidades: List[float]

class Input(BaseModel):
    taxa: float
    cotas: List[Dia]

@app.post("/calcular")
def calcular_taxa(data: Input):
    M = len(data.cotas[0].quantidades)  
    resultado = [0.0] * M
    
    for dia in data.cotas:
        for j in range(M):
            resultado[j] += (dia.quantidades[j] * dia.valor * data.taxa) / 252
    
    return resultado
