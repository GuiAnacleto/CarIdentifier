from app import app
from flask import render_template, redirect, url_for, session, jsonify
from app.service.identifier import identifier
from app.service.time import time

@app.route('/camera/<int:id>')
#@spec.validate(resp=Response(HTTP_200=StatusTransito))
def get_camera(id):
    """Retorna se a camera identificou algum veículo esperando """
    try:
        dic = {
            'id_semafaro': id,
            'carro_esperando': identifier(id),
            'data': time()
        }
    except Exception as e:
        print("Erro: ", e)
        dic = {
            'id_semafaro': id,
            'carro_esperando': True,
            'data': "Sunday-01-2022 03:00:00"
        }

    return jsonify(dic)

    

