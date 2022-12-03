from pydantic import BaseModel

class StatusTransito(BaseModel):
    id_semaforo: int
    carro_esperando: bool
    data: str

class Erro(BaseModel):
    Error : str
