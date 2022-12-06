import sqlite3
import pandas as pd

#Retona um DF com toda informação da tabela
def selectCarTraffic():
    try:
        sqliteConnection = sqlite3.connect('DBSR4001.db')
        cursor = sqliteConnection.cursor()

        df = pd.read_sql_query("SELECT * FROM carTraffic", sqliteConnection)
        print("Select successfully executed")
        cursor.close()
        return df

    except sqlite3.Error as error:
        print("Failed to select carTraffic table:", error)

#Retona um DF com toda informação da tabela
def selectTimeTable():
    try:
        sqliteConnection = sqlite3.connect('DBSR4001.db')
        cursor = sqliteConnection.cursor()

        df = pd.read_sql_query("SELECT * FROM timeTable", sqliteConnection)
        print("Select successfully executed")
        cursor.close()
        return df

    except sqlite3.Error as error:
        print("Failed to select carTraffic table:", error)