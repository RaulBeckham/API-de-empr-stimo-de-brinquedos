from domain.usuario import Usuario
from domain.sala import Sala
from domain.reserva import Reserva
from repositories.memory import db


def criar_crianca(nome: str, email: str):
    new_crianca = criancaCreate(id=db.next_crianca_id, nome=nome, idade=0) 
    db.crianca[db.next_crianca_id] = new_crianca

def listar_criancas():
    return list(db.crianca.values())


def criar_brinquedo(nome: str, categoria: str):
    new_brinquedo = brinquedoCreate(id=db.next_brinquedo_id, nome=nome, categoria=categoria) 
    db.brinquedo[db.next_brinquedo_id] = new_brinquedo

def listar_brinquedos():
    return list(db.brinquedo.values())

def criar_emprestimo(crianca_id: int, brinquedo_id: int, datas: str, status: str, multa: float):
    new_emprestimo = emprestimoCreate(id=db.next_emprestimo_id, crianca_id=crianca_id, brinquedo_id=brinquedo_id, datas=datas, status=status, multa=multa) 
    db.emprestimo[db.next_emprestimo_id] = new_emprestimo

def listar_emprestimos():
    return list(db.emprestimo.values())

def listar_emprestimos_por_crianca(crianca_id: int):
    return [emprestimo for emprestimo in db.emprestimo.values() if emprestimo.crianca_id == crianca_id]

