import requests
import json

def enviaCronograma(dict):
  PORT = ""
  ID = dict.get("id_semaforo")
  #verificar se o periodo vamos passar um por vez ou em lista em uma só requisicao
  data = {"diaDaSemana": {dict.get("diaDaSemana")}, 
          "duracaoMinutos": 60, 
          "horaInicial": {dict.get("horaInicial")}, 
          "tempoAmarelo": 5,
          "tempoVerde": {dict.get("tempoVerde")},
          "tempoVermelho": {dict.get("tempoVermelho")}
          }

  requisicao = requests.put(f"localhost:{PORT}/{ID}", data=data)

  if requisicao.status_code == 200:
    return requisicao.json()
  else:
    return requisicao.status_code
