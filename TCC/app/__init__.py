import socket
from app.config import config
from flask import Flask
from colored import fg
from flask_pydantic_spec import FlaskPydanticSpec

# Define o Aplicativo
app = Flask("app")
spec = FlaskPydanticSpec('flask', title='Vehicle Identifier')
spec.register(app)

# Configura as Variaveis de ambiente
if socket.gethostname() in ['envio.vps']:
    print(fg('green') + "Utilizando as Configurações de Produção")
    app.config.from_object(config.ProductionConfig)
else:
    print(fg('blue') + "Utilizando as Configurações de Produção")
    app.config.from_object(config.DevelopmentConfig)

#Importa todos os Controllers
from app.controllers import *
