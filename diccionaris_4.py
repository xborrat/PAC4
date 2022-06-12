"""
Modul que conté les funcions específiques i codi per resoldre l'exercici 4:
Creació i neteja de diccionaris de jugadors.
"""
import pandas as pd



def players_dict(df: pd.DataFrame, ids: list, cols: list) -> dict:
    """- df: dataframe que conté les dades
    - ids: llista d’identificador “sofifa_id”
    - cols: llista de columnes de les que volem informació
    Retorna un diccionari on la clau sera l'identificador i el valor un altre diccionari
    amb les columnes seleccionades com a clau i la llista de puntuacions com a valor"""

    diccionari = {}
    for id in ids:
        dict_col = {}
        for col in cols:
            dict_col.update({col: df.loc[df.sofifa_id == id, col].to_list()})
        diccionari.update({id: dict_col})
    return diccionari


def clean_up_players_dict(player_dict: dict, col_query: list) -> dict:
    """- player_dict: diccionari amb el formato de l’apartat (a) players_dict
    - col_query: llista de tuples amb detalls sobre la información que cal simplificar"""

    for col, query in col_query:
        for id, data in player_dict.items():
            for key, value_list in data.items():
                if key == col:
                    if query == "one":
                        player_dict[id][key] = value_list[0:1]

                    elif query == "del_rep":
                        # Posada a pla de la llista de cadenes.
                        flat_list = list(
                            set(" ".join(value_list).replace(",", "").split(" "))
                        )
                        player_dict[id][key] = flat_list
                    else:
                        print("error")
    return player_dict


if __name__ == "__main__":
    import preprocess as pre
    import pprint

    df = pre.join_datasets_year("data", list(range(2016, 2019)))
    # El diccionari construït amb la funció de l'apartat 4a amb la informació de les columnes ["short_name", "overall",
    # “potential”, "player_positions", "year"] i els ids = [226328, 192476, 230566].

    a = players_dict(
        df,
        [226328, 192476, 230566],
        ["short_name", "overall", "potential", "player_positions", "year"],
    )
    pprint.pprint(a)
    print('------------------------------------------------------------------------')

    # La query que passaríeu a la funció de l'apartat 4b per netejar aquest diccionari.
    print("La query que passaríeu a la funció de l'apartat 4b per netejar aquest diccionari:")
    print("('short_name', 'one'), ('player_positions', 'del_rep')")

    print('------------------------------------------------------------------------')
    print('Diccionari net')
    b = clean_up_players_dict(
        a, [("short_name", "one"), ("player_positions", "del_rep")]
    )

    pprint.pprint(b)
