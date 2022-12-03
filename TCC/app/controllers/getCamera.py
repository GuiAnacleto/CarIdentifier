from app import app, spec
from flask import jsonify
from app.service.identifier import identifier
from app.service.time import time
from app.service.insertDataDatabase import updateSqliteTable
from ..model.statusClassModel import StatusTransito
from flask_pydantic_spec import Response, Response, FlaskPydanticSpec


@app.route('/camera/<int:id>')
@spec.validate(resp=Response(HTTP_200=StatusTransito))
def get_camera(id):
    """Retorna se a camera identificou algum veículo esperando """
    try:
        dic = {
            'id_semaforo': id,
            'carro_esperando': identifier(id),
            'data': time("string")
        }
    except Exception as e:
        print("Erro: ", e)
        dic = {
            'id_semaforo': id,
            'carro_esperando': True,
            'data': "Sunday-01-2022 03:00:00"
        }

    updateSqliteTable(dic)

    return jsonify(dic)

    

