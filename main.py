"""
Codi que resol exercici 2 a partir de les funcions que demana l'exercici 1 i que estan als moduls
preprocess i calculations
"""

import preprocess as pre
import calculations as calc


if __name__ == "__main__":
    df = pre.join_datasets_year("data/", list(range(2016, 2023)) )

    col_selection = ["short_name", "year", "age", "overall", "potential"]
    # EXERCICI 2C:

    # Els jugadors de nacionalitat belga menors de 25 anys màxim “potential” al futbol masculí.
    df_query1 = calc.find_rows_query(
        df,
        (["nationality_name", "age", "gender"], ["Belgium", (0, 24), "M"]),
        col_selection,
    ).reset_index()
    df_query1 = calc.find_max_col(df_query1, "potential", col_selection)
    print("Els jugadors de nacionalitat belga menors de 25 anys màxim “potential” al futbol masculí.")
    print(df_query1)

    df_query2 = calc.find_rows_query(
        df, (["gender", "age", "overall", "player_positions"], ["F", (29, 70), (86, 1000),"GK"]), col_selection
    ).reset_index(drop=True)
    print("---------------------------------------------------------------------")

    # Les porteres majors de 28 anys amb “overall” superior a 85 al futbol femení.
    print("Les porteres majors de 28 anys amb “overall” superior a 85 al futbol femení.")
    print(df_query2)
