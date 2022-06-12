"""
Modul que conte funcions per preprocesar els fitxers de dades.
"""
import os
import re
import pandas as pd



def read_add_year_gender(filepath: str, gender: str, year: int) -> pd.DataFrame:
    """filepath: string amb la ruta de l’arxiu que volem llegir
    - gender: 'M' o 'F' (segons les sigles de “Male” or “Female”)
    - year: Any al que corresponen les dades en format XXXX (per exemple, 2020)
    - Llegeix una estructura dataframe i li afegeix una columna de 'gender' i una de year"""
    dataset = pd.read_csv(filepath,low_memory=False)
    dataset["gender"] = gender
    dataset["year"] = year
    return dataset


def join_male_female(path: str, year: int) -> pd.DataFrame:
    """- path: ruta a la carpeta que conté les dades
    - year: any del que es volen llegir les dades, format XXXX (per exemple, 2020)
    buscar fitxers a la carpeta que  continguin en el nom  l'any introduit com a paràmetre
    també busca en el nom si el fitxer conté  dades  female/no female. Amb la informació
    de l'any i el sexe cridarà a la funcio read_year_gender.
    Finalment es fusionaran els fitxers de la carpeta escollida que es refereixin a l'any escollit
    """

    year_str_xx = str(year)[
        -2:
    ]  # Extracció de les 2 ultimes xifres de l'any introduit.
    gender = ""
    datasets_to_join = []
    with os.scandir(path) as file_list:
        for file in file_list:
            if year_str_xx in file.name:
                if re.match(".*female.*", file.name):
                    gender = "F"
                else:
                    gender = "M"
                datasets_to_join.append(read_add_year_gender(file, gender, year))
    return pd.concat(datasets_to_join).reset_index(drop=True)


def join_datasets_year(path: str, years: list) -> pd.DataFrame:
    """- path: ruta a la carpeta que conté les dades
    - years: llista d’anys que es volen incloure en el dataframe, en format [XXXX,...]
    Uneix els datasets corresponents als anys de la llista"""
    datasets_to_join = []
    for every_year in years:
        datasets_to_join.append(join_male_female(path, every_year))
    return pd.concat(datasets_to_join).reset_index(drop=True)
