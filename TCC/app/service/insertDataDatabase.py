import sqlite3
from datetime import datetime, date

def updateSqliteTable(qtdCar):
    try:
        sqliteConnection = sqlite3.connect('../database/DBSR4001.db')
        cursor = sqliteConnection.cursor()

        currentDateAndTime = datetime.now()
        currentHour = currentDateAndTime.hour

        today = date.today()
        todayDate = today.strftime("%d/%m/%Y")

        cursor.execute(f"SELECT qtd_car from trafficHover where date = {todayDate} AND open_time = {currentHour}")
        qtdCarAtual = cursor.fetchone()
        qtdCarNova = qtdCarAtual + qtdCar

        cursor.execute(f"Update trafficHover set qtd_car = {qtdCarNova} where open_time = {currentHour}")
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")