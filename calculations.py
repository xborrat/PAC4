"""
Modul on hi les funcions necessaries i calculs per els exercicis 1,2 i 3.
"""
import re
import pandas as pd



def find_max_col(df: pd.DataFrame, filter_col: str, cols_to_return: list) -> pd.DataFrame:
    """- df: dataframe que conté les dades
    - filter_col: nom de la columna de la que volem saber el màxim - cols_to_return: llista de columnes que cal retornar
    Busca la fila amb el valor maxim de la columna que escollim "filter_col" i en retorna les columnes insertades als
    parametres "cols_to_return".
    """
    filter = df[filter_col] == df[filter_col].max()
    return df.loc[filter, cols_to_return]
    # return df.loc[[df[filter_col].idxmax(axis=0)], cols_to_return]


def find_rows_query(df: pd.DataFrame, query: tuple, cols_to_return: list) -> pd.DataFrame:
    """- df: dataframe que conté les dades
    - query: tupla que conté la query
    - cols_to_return: llista de columnes que cal retornar
    Funció que realiza consultes: La query en format tupla te 2 components:
        Primer component: les columnes que volem utilitzar per filtrar
        Segon component: els valors corresponents a les columnes anterior que volem seleccionar
        En el cas de una variable tipus string el mateix valor i en cas de variable numérica l'interval.
    També escollirem de les files seleccionades quines columnes volem seleccionar també.
    """

    for columna, valor in zip(query[0], query[1]):
        if df[columna].dtypes.name == 'object':
            df = df[df[columna] == valor]

        elif (df[columna].dtypes.name == 'float64') or (df[columna].dtypes.name == 'int64'):
            df = df[(df[columna] >= valor[0]) & (df[columna] <= valor[1])]

        else:
            print('La columna no conté ni nombres ni cadenes')
    df_to_return = df[cols_to_return]
    return df_to_return


def calculate_bmi(df: pd.DataFrame, gender: str, year: int, cols_to_return: list) -> pd.DataFrame:
    """- df: dataframe que conté les dades
    - gender: gènere que volem estudiar
    - year: any que volem estudiar en format XXXX (per exemple 2020)
    - cols_to_return: llista de columnes que cal retornar (sense columna BMI)
    Donat un dataframe es crea un subset amb un any i un sexe escollit. D'aquest subset
    es calcula el BMI i s'afegeix com a columna.
    També escollirem de les files seleccionades quines columnes volem seleccionar també.
    """
    df = df[(df.gender == gender) & (df.year == year)]
    df['BMI'] = df.weight_kg / (df.height_cm / 100) ** 2
    df_list = df[cols_to_return]
    return pd.concat([df.BMI, df_list], axis=1)


def extractor(url: str) -> str:
    """Accepta una el nom abrebiat del pais pel qual juga el jugador a partir de la url
    de la seva bandera. Funció que accepta una string(url) i extreu amb regex i slice
    el codi de 2 o 4 caràcters de cada pais."""
    return re.search(r's\/.*', url).group()[2:-4]
