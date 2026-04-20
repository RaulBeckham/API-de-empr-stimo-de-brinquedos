from pydantic import BaseModel

class criancaCreate(BaseModel):
    id: int
    nome: str
    idade: int

class criancaOut(BaseModel):
    id: int
    nome: str
    idade: int