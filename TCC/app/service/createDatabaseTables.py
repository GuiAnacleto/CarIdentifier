
import sqlite3

def createTables():
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('../database/DBSR4001.db')
    
    # cursor object
    cursor_obj = connection_obj.cursor()
    
    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS trafficHover")
    
    # Creating table
    table = """ CREATE TABLE trafficHover (
                id INTEGER PRIMARY KEY,
                id_semaforo int,
                carro_esperando  int,
                date date
            ); """

    cursor_obj.execute(table)
    
    print("Table is Ready")
    
    # Close the connection
    connection_obj.close()

if __name__ == '__main__':
    createTables()