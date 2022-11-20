from app import app
from flask import render_template, redirect, url_for, session, jsonify

@app.route('/mock/<status>')
#@spec.validate(resp=Response(HTTP_200=StatusTransito, HTTP_400=Erro))
def get_mock(status):
    """Endpoint para teste de verificação mockados"""
    try: 
        if status == "true":
            dic = {
                'id_semafaro': 1000,
                'carro_esperando': True,
                'data': "Sunday-01-2022 03:00:00"
            }
        elif status == "false":
            dic = {
                'id_semafaro': 1000,
                'carro_esperando': False,
                'data': "Sunday-01-2022 03:00:00"
            }
        return jsonify(dic)

    except Exception as e:
        print("Erro: ", e)
        return jsonify({'Erro': 'Status não encontrado'}), 404
