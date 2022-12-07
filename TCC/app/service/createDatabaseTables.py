
import sqlite3

def createTables():
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('../../DBSR4001.db')
    
    # cursor object
    cursor_obj = connection_obj.cursor()
    
    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS trafficHover")
    cursor_obj.execute("DROP TABLE IF EXISTS carTraffic")
    cursor_obj.execute("DROP TABLE IF EXISTS timeTable")
    
    table2 = """ CREATE TABLE carTraffic (
                id INTEGER PRIMARY KEY,
                id_semaforo int,
                quantidade_total  int,
                dia_semana int,
                data text,
                hora int
            ); """
    
    table3 = """ CREATE TABLE timeTable (
                id INTEGER PRIMARY KEY,
                id_semaforo text,
                diaDaSemana int,
                horaInicial int,
                tempoVerde  int,
                numAtualizacao int,
                mediaQuantidade int,
                mediaAntiga int,
                tempoVerdeAntigo int,
            );"""            

    cursor_obj.execute(table2)
    cursor_obj.execute(table3)

    print("Tables is Ready")
    
    # Close the connection
    connection_obj.close()

if __name__ == '__main__':
    createTables()
