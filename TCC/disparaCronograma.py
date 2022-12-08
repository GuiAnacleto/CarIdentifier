import json
from flask import requests
from app.service.selectTables import selectTimeTable


def enviaCronograma():
  PORT = "8080"

  dfTimeTable = selectTimeTable()

  ID = dfTimeTable['id_semaforo']
  #verificar se o periodo vamos passar um por vez ou em lista em uma só requisicao
  data = {"diaDaSemana": {dfTimeTable["diaDaSemana"] + 1},
          "horaInicial": {dfTimeTable["horaInicial"]}, 
          "tempoVerde": {dfTimeTable["tempoVerde"]}
          }

  requisicao = requests.put(f"localhost:{PORT}/cronograma/{ID}", data=data)

  if requisicao.status_code == 200:
    return requisicao.json()
  else:
    return requisicao.status_code


if __name__ == '__main__':
    enviaCronograma()