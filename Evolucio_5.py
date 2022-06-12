"""
Modul que conté  el condi necessari i les funcions especifiques per
resoldre l'exercici 5: Evolució dels futbolistes
"""

import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import diccionaris_4 as dic
import preprocess as pre



def top_average_column(data: dict, identifier: str, col: str, threshold: int) -> list:
    """- data: diccionari “net” que conté la informació de diversos sofifa_id
    - identifier: columna/clau que es fara servir com identificador
    - col: nom d’una columna/clau numérica
    - threshold: mínim número de dades necessàries"""
    llista = []
    for sofifa_id, data_dict in data.items():
        if (len(data_dict[col]) >= threshold) and not(np.isnan(data_dict[col])).any():
            llista.append((data_dict[identifier][0], np.mean(data_dict[col]),
                           {'value': data_dict[col], 'year': data_dict['year']}))
    # La funcio sort no funciona be NaN per això filtro els possibles NaNs que puguessin quedar.
    return sorted(llista, key=lambda i: -np.inf if np.isnan(i[1]) else i[1], reverse=True)


if __name__ == '__main__':

    # Creacio del dataset amb tots els jugadors de 2016 a 2023
    df = pre.join_datasets_year('data/', list(range(2016, 2023)))

    # Creacio del diccionari amb movement_print_speed.
    a = dic.players_dict(df, df.sofifa_id.unique(), ['short_name', 'movement_sprint_speed', 'year'])

    # Nejeja del diccionari.
    b = dic.clean_up_players_dict(a, [('short_name', 'one')])

    # Crida a la funcio amb evolució dels 4 futbolistes amb millor mitjana de movement_sprint_speed entre el 2016 i el 2022 (inclosos).
    # Utilitzeu “short_name” com a identificador i mostreu el resultat per pantalla.

    c = top_average_column(data=b, identifier='short_name', col='movement_sprint_speed', threshold=2)

    pprint.pprint(c[0:4])  # Els 4 millors futbolistes en quant a mitjana.
    print('-----------------------------------------------------------------------')
    # Representeu gràficament l'evolució obtinguda.

    dict = {}
    # Creació d'un diccionari on hi haurà les llistes de tuplas(valor, any)
    for i in c[0:4]:
        dict.update({i[0]: list(zip(i[2]['value'], i[2]['year']))})

    print(dict)
    print('-----------------------------------------------------------------------')
    # Creació d'un dataframe a partir del diccionari.
    df = pd.DataFrame([])
    for player, data in dict.items():
        for tupla in data:
            df.loc[tupla[1], player] = tupla[0]

    df.sort_index(inplace=True)
    print(df)
    print('-----------------------------------------------------------------------')
    # Generació del gràfic
    ax = df.plot(marker="o", linestyle='--')
    plt.title('Players, sprint evolution ')
    plt.ylim([90, 98])

    plt.xticks(rotation='vertical')
    ax.set_xticks([2016, 2017, 2018, 2019, 2020, 2021, 2022])
    plt.subplots_adjust(bottom=0.15)
    plt.show()
