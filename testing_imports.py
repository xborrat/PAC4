# pylint: skip-file
# Poned aquí los imports de las funciones que hay que testear.

import os
from typing import Dict, Union, Any
import matplotlib.pyplot as plt
import seaborn as sns
import re
import statistics
import pandas as pd
from calculations import find_max_col, find_rows_query, calculate_bmi, extractor
from preprocess import read_add_year_gender, join_male_female, join_datasets_year
from Evolucio_5 import top_average_column
from diccionaris_4 import clean_up_players_dict, players_dict
