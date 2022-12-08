from datetime import datetime
from app.service.selectTables import selectCarTraffic, selectTimeTable

dds = datetime.now().strftime("%w")

df_1 = selectCarTraffic(1, dds)
df_2 = selectCarTraffic(2, dds)

cronograma_df1 = selectTimeTable(1, dds)
cronograma_df2 = selectTimeTable(2, dds)

media_antiga1
media_antiga2

"""

media_antiga1 = df_1["media"]
media_antiga2 = df_2["media"]

qt_1 = df_1["quantidade_total"]
qt_2 = df_2["quantidade_total"]

media1 = df_1["quantidade_total"]/cronograma_df1["tempoVerde"]
media2 = df_2["quantidade_total"]/cronograma_df2["tempoVerde"]


valida se a nova media foi maior que a media antiga
    if >= media_antiga1: 
        retiro X do semaforo com menor media e aumenta o outro
        e salva no banco como media e media antiga

    else:
        adiciona X/2 de tempo no menor e diminui no outro"""

