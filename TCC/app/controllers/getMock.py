from app import app, spec
from flask import jsonify
from app.service.insertDataDatabase import updateSqliteTable
from ..model.statusClassModel import StatusTransito, Erro
from flask_pydantic_spec import Response, Response, FlaskPydanticSpec


@app.route('/mock/<status>')
@spec.validate(resp=Response(HTTP_200=StatusTransito, HTTP_400=Erro))
def get_mock(status):
    """Endpoint para teste de verificação mockados"""
    try: 
        if status == "true":
            dic = {
                'id_semaforo': 1000,
                'carro_esperando': 1,
                'data': "Sunday-01-2022 03:00:00"
            }
        elif status == "false":
            dic = {
                'id_semaforo': 1000,
                'carro_esperando': 0,
                'data': "Sunday-01-2022 03:00:00"
            }

        updateSqliteTable(dic)

        return jsonify(dic)

    except Exception as e:
        print("Erro: ", e)
        return jsonify({'Erro': 'Status não encontrado'}), 404
