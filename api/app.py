from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec
from datetime import datetime
from pytz import timezone

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='CarIdentifier')

spec.register(server)

@server.get('/camera')
def get_camera():
    hora_atual = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')

    hora = hora_atual.astimezone(fuso_horario)
    return hora.strftime("%A-%m-%Y %H:%M:%S")

server.run()