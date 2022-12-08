import pandas as pd
from datetime import datetime
from app.service.selectTables import selectCarTraffic, selectTimeTable, updateSqliteTableTimeTableOtimizacao


def ajustaCronograma(id):

    dds = datetime.now().strftime("%w")
    horaInicial = datetime.now().strftime("%H")

    df_1 = selectCarTraffic(id, dds)
    #df_2 = selectCarTraffic(2, dds)

    cronograma_df1 = selectTimeTable(id, dds)
    #cronograma_df2 = selectTimeTable(2, dds)

    media_antiga1 = cronograma_df1["mediaAntiga"]
    #media_antiga2 = cronograma_df2["mediaAntiga"]

    qt_1 = df_1["quantidade_total"]
    #qt_2 = df_2["quantidade_total"]

    media1 = qt_1/cronograma_df1["tempoVerde"]
    #media2 = qt_2/cronograma_df2["tempoVerde"]
    
    if media1 > media_antiga1:
        #Quanto tempo vamos aumentar?
        #10%
        tempoNovo = round((cronograma_df1["tempoVerde"] + cronograma_df1["tempoVerde"] * 0.10)*1000)

        updateSqliteTableTimeTableOtimizacao(id, dds, horaInicial, tempoNovo, media1, cronograma_df1["tempoVerde"])
    else:
        updateSqliteTableTimeTableOtimizacao(id, dds, horaInicial, cronograma_df1["tempoVerdeAntigo"], media_antiga1, cronograma_df1["tempoVerde"])


if __name__ == '__main__':
    ajustaCronograma()
