
# PAC4 Programació per a Ciència de dades. UOC màster en ciència de dades.

Aquest projecte vol resoldre els exercicis i preguntes incloses al PAC4.

Inclou:
- Carpeta principal: 
    - fitxers .py dels exercicis i moduls de funcions
    - fitxer .csv output exercici 6
    - fitxer pdf explicació exercici6 
    - requirements.txt
    - LICENCSE.txt 
    - README.md.
    - testing_imports.py
- Carpeta de dades: `data`
- Carpeta de test: `test`


## Authors

- Xavier Borrat Frigola


## Installation

Instalació des de fitxer PAC4_xavier_borrat.zip

1. Descomprimir document zip
2. Crear un entorn virtual (optional)
3. `pip install -r requirement.txt`





    
## Documentation

En aquest apartat es decriu com utilitzar els fitxers per verificar les respostes i les tasques de la PAC.

### Exercici 1:

Creació funció `read_add_year_gender` , `join_male_female` i  `join_datasets_year`. Es troben al modul `preprocess.py` 

### Exercici 2:
Creació funció `find_max_col` i  `find_rows_query` . Es troben al modul `calculations.py`

Apartat C:
Crear les queries per les funcions `find_max_col` i  `find_rows_query` que seleccionin:
- Els jugadors de nacionalitat belga menors de 25 anys màxim “potential” al futbol masculí.

- Les porteres majors de 28 anys amb “overall” superior a 85 al futbol femení.

Resposta: Execució fitxer `main.py` 

### Exercici 3:
Creació de la funció  `calculate_bmi` continguda en el mateix modul `bmi_3.py`

Per a la visualització de les gràfiques dels apartats a i b cal executar el fitxer `bmi_3.py`.

Es creen les dues gràfiques. Per veure la segona cal tancar al primera. 

RESPOSTA APARTAT A: Hi ha un país amb un jugador a punt d'entrar en rangs d'obesitat mórbida. 
Es un jugador angles:Saheed Adebayo Akinfenwa. S'ha de tenir en compte però que el BMI amb persones 
amb molta massa muscular no permet utilitzar els mateixos rangs d'obesitat mórbida o sobrepés.

RESPOSTA APARTAT B: Gràfica de la proporcio de Sobrepés en Dones any 2020  Edat (25-34 anys). Comparant  
Futbolistes Professionals VS Població General.


### Exercici 4:
 Creació de la funció `players_dict` i `clean_up_players_dict` dintre le mateix modul `diccionaris_4.py`.

 Utilització de les funcions del mateix modul per resoltre exercici 4 apartat c executant el modul `diccionaris_4.py`.

La query que passaríeu a la funció de l'apartat 4b(`clean_up_players_dict`) per netejar el diccionari:

    `('short_name', 'one'), ('player_positions', 'del_rep')`


### Exercici 5:
Creació de la funció `top_average_column`  dintre le mateix modul `Evolucio_5.py`.

Per utilitzar l'anterior funció i representar graficament l'evolució dels 4 millors jugadors pel que fa a la 
característica movement_sprint_speed s'ha d'executar el modul `Evolucio_5.py`


### Exercici 6:

Per realitzar el que demana l'enunciat de l'exercici 6 cal executar el modul `d_fence_6.py`. Tot i la Utilització de 
llibreries de computació paral·lela l'execució és molt lenta per això s'ha inclós a la carpeta un exemple en 
format .csv de l'output del modul per a competició masculina. 


Explicació de com utilitzar el mòdul i informació complerta de les aproximacions utilitzades
en els requeriments de l'exercici 6 al document pdf `Exercici_6_info.pdf`
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Running Tests

Instal·lació

```bash
 pip install HTMLTestRunner-rv

```
Executar test public:
`python3 -m tests.test_public`

Executar test custom fet per l'alumne:
` python3 -m tests.test_custom`

Per a poder executar els tests s'han inclós les llibreries necessaries al modul:

`testing_imports.py`
