import sqlite3
from datetime import datetime, date

def updateSqliteTable(dict):
    try:
        sqliteConnection = sqlite3.connect('../database/DBSR4001.db')
        cursor = sqliteConnection.cursor()

        """currentDateAndTime = datetime.now()
        currentHour = currentDateAndTime.hour

        today = date.today()
        todayDate = today.strftime("%d/%m/%Y")

        cursor.execute(f"SELECT qtd_car from trafficHover where date = {todayDate} AND open_time = {currentHour}")
        qtdCarAtual = cursor.fetchone()
        qtdCarNova = qtdCarAtual + qtdCar"""

        cursor.execute(f"Update trafficHover set id_semaforo = {dict.get('id_semaforo')}, carro_esperando = {dict.get('carro_esperando')}, date = {dict.get('data')}")
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def updateSqliteTableCarTraffic(dict):
    try:
        sqliteConnection = sqlite3.connect('../database/DBSR4001.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"Update carTraffic set id_semaforo = {dict.get('id_semaforo')}, quantidade_total = {dict.get('quantidade_total')}, dia_semana = {dict.get('dia_semana')}, data = {dict.get('data')}, hora = {dict.get('hora')}")
        sqliteConnection.commit()
        print("Record Updated carTraffic successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite carTraffic table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            
def updateSqliteTableTimeTable(dict):
    try:
        sqliteConnection = sqlite3.connect('../database/DBSR4001.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"Update tableTime set id_semaforo = {dict.get('id_semaforo')}, diaDaSemana = {dict.get('diaDaSemana')}, horaInicial = {dict.get('horaInicial')}, num_atualizacao = {dict.get('num_atualizacao')}, tempoVerde = {dict.get('tempoVerde')}, tempoVermelho = {dict.get('tempoVermelho')}")
        sqliteConnection.commit()
        print("Record Updated tableTime successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite tableTime", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
