from fastapi import APIRouter
from schemas import brinquedo_schema

router = APIRouter()

@router.post("/brinquedos")
def criar_brinquedo(brinquedo: brinquedo_schema.brinquedoCreate):
    new_brinquedo = criar_brinquedo(id=brinquedo.id, nome=brinquedo.nome, categoria=brinquedo.categoria)

@router.get("/brinquedos")
def listar_brinquedos():
    return listar_brinquedos()