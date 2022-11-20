from datetime import datetime
from pytz import timezone

def time():
    hora_atual = datetime.now()
    fuso = timezone('America/Sao_Paulo')

    hora = hora_atual.astimezone(fuso)

    return hora.strftime("%A-%m-%Y %H:%M:%S")
