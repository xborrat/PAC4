"""
Modul on hi ha les funcions necessaries i el codi per resoldre l'exercici 6:
TROBAR L'ALINEACIÓ DE DEFENSA IDEAL.
"""

import concurrent.futures
import re
import itertools
import pandas as pd
import preprocess as pre



def overall_list(competicio: str, posicio: str) -> list:
    """Rep dues cadenes (tipus competicio i posició al camp i torna una llista amb els millors jugadors amb
    aquestes característiques agafant com a referencia el parametre overall"""
    df = pre.join_datasets_year('data/', [2022])
    df.sort_values('overall', inplace=True, ascending=False)  # ordeno de forma descendent segons 'overall'
    # Seleccio del tipus de comptició (M,F, veterans) i la posició (CB,LB,RB) en funció dels paràmetres passats
    if competicio == 'M' or competicio == 'F':
        dt = \
            df[(df.gender == competicio) & (
                df.player_positions.apply(lambda x: re.search(r".*" + re.escape(posicio), x)))][
                'sofifa_id']
    elif competicio == 'vet':
        dt = \
            df[(df.age >= 30) & (df.player_positions.apply(lambda x: re.search(r".*" + re.escape(posicio), x)))][
                'sofifa_id']

    return dt.to_list()[0:20]  # limit a 20 primers amb overall més alt.


def line_generator(competicio: str) -> list:
    """Accepta el paràmetre tipus competició i utilitzant la funció overall_list es creen 4 llistes amb les 4 posicions.
    amb la combinació de les quatre llistes es generen multiples llistes de 4 jugadors amb la condició que en una
    mateixa llista no es repeteixi el jugador i que no hi hagi duplicats on coincideixin els 4 jugadors
    en la mateixa posició"""
    a = []
    ws = overall_list(competicio, 'LB')
    xs = overall_list(competicio, 'CB')
    ys = overall_list(competicio, 'CB')
    zs = overall_list(competicio, 'RB')

    for w in ws:
        for x in xs:
            for y in ys:
                for z in zs:
                    line_d = list(set([w, x, y, z]))
                    if len(line_d) == 4:
                        a.append(line_d)
    a.sort()
    return list(k for k, _ in
                itertools.groupby(a))  # retorna una llista amb les llistes de totes les combinacions de 4 jugadors/res


def line_features(linia: list, database: pd.DataFrame) -> pd.DataFrame:
    """
       :param competicio: accepta el tipus de competició
       :return: retorna un dataframe d'una linea amb els noms dels jugadors d'una linia defensiva i els les puntuacions
       sumades de les seves característiques com atac, defensa, possessió de pilota en cada posició i també la suma
       total de les puntuacions per linia defensiva.
       """
    def_line_features = pd.DataFrame([])

    dt = pd.DataFrame(index=[],
                      data={'agregador': [], 'short_name': [], 'sofifa_id': [], 'RB_attack': [], 'CB_attack': [],
                            'LB_attack': [],
                            'ball_control': [], 'RB_defense': [], 'CB_defense': [], 'LB_defense': []})
    for position, sofifa_id in enumerate(linia):
        if position == 0:
            dic_line = {'agregador': 1,
                        'sofifa_id': sofifa_id,
                        'short_name': database.short_name[database.sofifa_id == sofifa_id].values[0],
                        'LB_attack': database.movement_acceleration[database.sofifa_id == sofifa_id].values[0],
                        'LB_defense': database.defending[database.sofifa_id == sofifa_id].values[0],
                        'ball_control': database.skill_ball_control[database.sofifa_id == sofifa_id].values[0]
                        }
            # dt=dt.append(dic_line, ignore_index= True)
            dt = pd.concat([dt, pd.DataFrame(dic_line, index=[1])], ignore_index=True, axis=0)
        if position == 1 or position == 2:
            dic_line = {'agregador': 1,
                        'sofifa_id': sofifa_id,
                        'short_name': database.short_name[database.sofifa_id == sofifa_id].values[0],
                        'CB_attack': database.attacking_crossing[database.sofifa_id == sofifa_id].values[0],
                        'CB_defense': database.defending_marking_awareness[database.sofifa_id == sofifa_id].values[0],
                        'ball_control': database.skill_ball_control[database.sofifa_id == sofifa_id].values[0]
                        }
            dt = pd.concat([dt, pd.DataFrame(dic_line, index=[1])], ignore_index=True, axis=0)

        if position == 3:
            dic_line = {'agregador': 1,
                        'sofifa_id': sofifa_id,
                        'short_name': database.short_name[database.sofifa_id == sofifa_id].values[0],
                        'RB_attack': database.skill_long_passing[database.sofifa_id == sofifa_id].values[0],
                        'RB_defense': database.mentality_positioning[database.sofifa_id == sofifa_id].values[0],
                        'ball_control': database.skill_ball_control[database.sofifa_id == sofifa_id].values[0]
                        }
            dt = pd.concat([dt, pd.DataFrame(dic_line, index=[1])], ignore_index=True, axis=0)
        agregated_lines = dt.groupby('agregador').agg({'short_name': ",".join,
                                                       'RB_attack': 'sum',
                                                       'RB_defense': 'sum',
                                                       'CB_attack': 'sum',
                                                       'CB_defense': 'sum',
                                                       'LB_attack': 'sum',
                                                       'LB_defense': 'sum',
                                                       'ball_control': 'sum'
                                                       })

    def_line_features = pd.concat([def_line_features, agregated_lines], ignore_index=True)
    def_line_features['Total'] = def_line_features.RB_attack + \
                                 def_line_features.RB_defense + \
                                 def_line_features.CB_attack + \
                                 def_line_features.CB_defense + \
                                 def_line_features.LB_attack + \
                                 def_line_features.LB_defense + \
                                 def_line_features.ball_control

    def_line_features.reset_index()

    return def_line_features


if __name__ == '__main__':

    # Per triar la competió s'ha de modificar la crida a la funció 'line_generator' amb valor
    # 'M' per competició masculina
    # 'F' per competició femenina
    # 'vet' competició de veterans

    df = line_generator('M')  #
    database = pre.join_datasets_year('data/', [2022])
    result = pd.DataFrame([])

    # Utilitzacio de computació paralela per optimització del temps de processat
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for linia in df:
            a = executor.submit(line_features, linia, database)
            result = pd.concat([result, a.result()], ignore_index=True)
        executor.shutdown()

    ordered_results = result.sort_values(by='Total', ascending=False).reset_index(
        drop=True)

    ordered_results.to_csv('d_fence_results_M.csv')
