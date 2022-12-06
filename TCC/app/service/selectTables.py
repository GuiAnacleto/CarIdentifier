import sqlite3

#Retona um DF com toda informação da tabela
def selectCarTraffic():
    try:
        sqliteConnection = sqlite3.connect('../../DBSR4001.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"SELECT * FROM carTraffic")
        data = cursor.fetchall()
        print(data)
        print("Select successfully executed")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select timeTable table", error)