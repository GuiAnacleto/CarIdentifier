from flask import requests
import json

def enviaCronograma(dict):
  PORT = "8080"
  ID = dict.get("id_semaforo")
  #verificar se o periodo vamos passar um por vez ou em lista em uma só requisicao
  data = {"diaDaSemana": {dict.get("diaDaSemana")}, 
          "duracaoMinutos": 60, 
          "horaInicial": {dict.get("horaInicial")}, 
          "tempoVerde": {dict.get("tempoVerde")}
          }

  requisicao = requests.put(f"localhost:{PORT}/cronograma/{ID}", data=data)

  if requisicao.status_code == 200:
    return requisicao.json()
  else:
    return requisicao.status_code
