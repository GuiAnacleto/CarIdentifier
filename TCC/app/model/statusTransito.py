from pydantic import BaseModel

class StatusTransito(BaseModel):
    id_semafaro: int
    carro_esperando: bool
    data: str