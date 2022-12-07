import sqlite3
import os
from datetime import datetime, date

def updateSqliteTableCarTraffic(dict):
    try:
        sqliteConnection = sqlite3.connect('DBSR4001.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"INSERT INTO carTraffic (id_semaforo, quantidade_total, dia_semana, data, hora) VALUES (?,?,?,?,?)", (dict.get('ID'), dict.get('quantidade_total'), dict.get('dia_semana'), dict.get('data'), dict.get('hora')))
        sqliteConnection.commit()
        print("Record Updated carTraffic successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite carTraffic table: ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            
def updateSqliteTableTimeTable(dict):
    try:
        sqliteConnection = sqlite3.connect('../database/DBSR4001.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"Update tableTime set id_semaforo = {dict.get('id_semaforo')}, diaDaSemana = {dict.get('diaDaSemana')}, horaInicial = {dict.get('horaInicial')}, num_atualizacao = {dict.get('num_atualizacao')}, tempoVerde = {dict.get('tempoVerde')}, mediaQuantidade = {dict.get('mediaQuantidade')}, mediaAntiga = {dict.get('mediaAntiga')}, tempoVerdeAntigo = {dict.get('tempoVerdeAntigo')} }")
        sqliteConnection.commit()
        print("Record Updated tableTime successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite tableTime", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
