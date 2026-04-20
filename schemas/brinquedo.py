from pydantic import BaseModel

class brinquedoCreate(BaseModel):
    id: int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool = True

class brinquedoOut(BaseModel):
    id: int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool = True