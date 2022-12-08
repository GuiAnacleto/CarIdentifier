import sqlite3
import pandas as pd

#Retona um DF com toda informação da tabela
def selectCarTraffic(id, dds):
    try:
        sqliteConnection = sqlite3.connect('DBSR4001.db')
        cursor = sqliteConnection.cursor()

        query = f"SELECT * FROM carTraffic WHERE id_semaforo = {id} AND dia_semana = '{dds}'"

        df = pd.read_sql_query(query, sqliteConnection)
        print("Select successfully executed")
        cursor.close()
        return df

    except sqlite3.Error as error:
        print("Failed to select carTraffic table:", error)

#Retona um DF com toda informação da tabela
def selectTimeTable(id, dds):
    try:
        sqliteConnection = sqlite3.connect('DBSR4001.db')
        cursor = sqliteConnection.cursor()

        query = f"SELECT * FROM timeTable WHERE id_semaforo = {id} AND diaDaSemana = '{dds}'"        

        df = pd.read_sql_query(query, sqliteConnection)
        print("Select successfully executed")
        cursor.close()
        return df

    except sqlite3.Error as error:
        print("Failed to select carTraffic table:", error)