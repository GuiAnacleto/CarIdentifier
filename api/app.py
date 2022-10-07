from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response
from pydantic import BaseModel
from utils import time

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Vehicle Identifier')
spec.register(server)

class Camera(BaseModel):
    id_semafaro: int
    carro_esperando: bool
    data: str


@server.get('/camera/<int:id>')
@spec.validate(resp=Response(HTTP_200=Camera))
def get_camera(id):
    """Retorna se a camera identificou algum veículo esperando  """
    #aqui será chamado o modelo de classificação que irá dizer se tem
    #carro parado ou não
    
    #em seguida o resultado será armazenado em um json e retornado como response
    try:
        dic = {
            'id_semafaro': id,
            'carro_esperando': True,
            'data': time()
        }
    except Exception as e:
        print("Error: ", e)
        dic = {
            'id_semafaro': id,
            'carro_esperando': True,
            'data': "Default"
        }

    return jsonify(dic)

server.run()