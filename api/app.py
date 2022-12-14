# from flask import Flask, jsonify
# from flask_pydantic_spec import FlaskPydanticSpec, Response
# from pydantic import BaseModel
# from utils import time
# from bumblebee import identifier


# server = Flask(__name__)
# spec = FlaskPydanticSpec('flask', title='Vehicle Identifier')
# spec.register(server)

# class StatusTransito(BaseModel):
#     id_semaforo: int
#     carro_esperando: bool
#     data: str

# class Erro(BaseModel):
#     Error : str

# @server.get('/camera/<int:id>')
# #@spec.validate(resp=Response(HTTP_200=StatusTransito))
# def get_camera(id):
#     """Retorna se a camera identificou algum veículo esperando  """
    
#     #aqui será chamado o modelo de classificação que irá dizer se tem
#     #carro parado ou não
    
#     #em seguida o resultado será armazenado em um json e retornado como response
#     try:
#         dic = {
#             'id_semaforo': id,
#             'carro_esperando': identifier(id),
#             'data': time()
#         }
#     except Exception as e:
#         print("Erro: ", e)
#         dic = {
#             'id_semaforo': id,
#             'carro_esperando': True,
#             'data': "Sunday-01-2022 03:00:00"
#         }

#     return jsonify(dic)

# @server.get('/mock/<status>')
# @spec.validate(resp=Response(HTTP_200=StatusTransito, HTTP_400=Erro))
# def get_mock(status):
#     """Endpoint para teste de verificação mockados"""
#     try: 
#         if status == "true":
#             dic = {
#                 'id_semaforo': 1000,
#                 'carro_esperando': True,
#                 'data': "Sunday-01-2022 03:00:00"
#             }
#         elif status == "false":
#             dic = {
#                 'id_semaforo': 1000,
#                 'carro_esperando': False,
#                 'data': "Sunday-01-2022 03:00:00"
#             }
#         return jsonify(dic)

#     except Exception as e:
#         print("Erro: ", e)
#         return jsonify({'Erro': 'Status não encontrado'}), 404


# server.run()
