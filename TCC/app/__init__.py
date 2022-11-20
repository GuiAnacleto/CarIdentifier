import os
import socket
import re
import sys
from app.config import config
from flask import Flask, session
from flask_pydantic_spec import FlaskPydanticSpec, Response
from pydantic import BaseModel
from colored import fg

# Define o Aplicativo
app = Flask("app")

# Configura as Variaveis de ambiente
if socket.gethostname() in ['envio.vps']:
    print(fg('green') + "Utilizando as Configurações de Produção")
    app.config.from_object(config.ProductionConfig)
else:
    print(fg('blue') + "Utilizando as Configurações de Produção")
    app.config.from_object(config.DevelopmentConfig)

#Importa todos os Controllers
from app.controllers import *