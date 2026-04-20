from fastapi import APIRouter
from schemas import emprestimo_schema

router = APIRouter()

@router.post("/emprestimos")
def criar_emprestimo(emprestimo: emprestimo_schema.emprestimoCreate):
    new_emprestimo = new_emprestimo(id=emprestimo.id, crianca_id=emprestimo.crianca_id, brinquedo_id=emprestimo.brinquedo_id, datas=emprestimo.datas, status=emprestimo.status, multa=emprestimo.multa)

@router.get("/emprestimos")
def listar_emprestimos():
    return listar_emprestimos()

@router.get("/emprestimos/{crianca_id}")
def listar_emprestimos_por_crianca(crianca_id: int):
    return listar_emprestimos_por_crianca(crianca_id)

