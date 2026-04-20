from pydantic import BaseModel

class emprestimoCreate(BaseModel):
    id: int
    crianca_id: int
    brinquedo_id: int
    datas: int
    status: str
    multa: float

class emprestimoOut(BaseModel):
    id: int
    crianca_id: int
    brinquedo_id: int
    datas: int
    status: str
    multa: float