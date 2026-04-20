from dataclasses import dataclasses

@dataclasses (frozen=True)
class Crianca:
    id:int
    nome:str
    idade:int
    responsavel:str