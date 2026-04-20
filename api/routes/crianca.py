from fastapi import APIRouter
from schemas import crianca_schema

router = APIRouter()

@router.post("/criancas")
def criar_crianca(crianca: crianca_schema.criancaCreate):
    new_crianca = new_crianca(id=crianca.id, nome=crianca.nome, idade=crianca.idade)

@router.get("/criancas")
def listar_criancas():
    return listar_criancas()

@router.get("/criancas/{crianca_id}")
def listar_crianca(crianca_id: int):
    crianca = db.crianca.get(crianca_id)
    if crianca:
        return crianca
    return {"message": "Criança não encontrada"}