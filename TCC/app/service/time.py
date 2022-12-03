from datetime import datetime
from pytz import timezone

def time(formato):
    hora_atual = datetime.now()
    fuso = timezone('America/Sao_Paulo')

    hora = hora_atual.astimezone(fuso)

    if formato == "string":
        return hora.strftime("%A-%m-%Y %H:%M:%S")
    else:
        return hora
