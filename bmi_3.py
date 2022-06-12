"""
Modul que conte les funcions específiques i el codi per executar-les en el context de l'exercici 3
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import preprocess as pre
import calculations as calc

if __name__ == '__main__':
    df = pre.join_datasets_year('data/', list(range(2016, 2023)))
    df['pais'] = df.nation_flag_url.apply(calc.extractor)
    df_ex3a = calc.calculate_bmi(df=df, gender='M', year=2022, cols_to_return=['pais', 'long_name']).reset_index()
    df_graf = df_ex3a.groupby('pais').aggregate(max)
    ax = sns.barplot(y=df_graf.index, x='BMI', data=df_graf).set(title='Max BMI vs Countries')
    plt.show()

    # RESPOSTA APARTAT A: Hi ha un país amb un jugador a punt d'entrar en rangs d'obesitat mórbida. Es un jugador angles:Saheed Adebayo Akinfenwa
    # S'ha de tenir en compte però que el BMI amb persones amb molta massa muscular no permet utilitzar els mateixos rangs d'obesitat
    # mórbida o sobrepés.

    df_ex3b_Total = calc.calculate_bmi(df=df, gender='F', year=2020, cols_to_return=['age']).reset_index()

    df_ex3b_filtrat = df_ex3b_Total[(df_ex3b_Total.age >= 25) & (df_ex3b_Total.age <= 34) & (df_ex3b_Total.BMI >= 25)]

    fut_bmi_total = df_ex3b_Total.BMI.count()

    fut_bmi_sobrepes = df_ex3b_filtrat.shape[0]

    ine_dt = pd.read_csv('data/fifa_BMI.csv', sep=';')

    print(ine_dt.iloc[1:3, 3].to_list())
    print(float(ine_dt.iloc[0, 3].replace(",", "")))

    poblacio_bmi_sobrepes = sum([float(i) for i in ine_dt.iloc[1:3, 3].to_list()])
    poblacio_bmi_total = float(ine_dt.iloc[0, 3].replace(",", ""))

    dict_BMI = {'Futbolistes': fut_bmi_sobrepes / fut_bmi_total,
                'Poblacio_general': poblacio_bmi_sobrepes / poblacio_bmi_total}

    df_graf2 = pd.DataFrame(dict_BMI, index=[0])

    ax = sns.barplot(data=df_graf2).set(
        title='Proporcio de Sobrepés  Dones any 2020  Edat (25-34 anys). \n Futbolistes '
              'Professionals VS Població General. ')
    plt.show()
