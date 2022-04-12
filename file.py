import pandas as pd
import json

df = pd.read_csv('./data/tocantins.csv')
df_tocantins = df[~df['municipio'].isna()]

tocantins_regioes = json.load(open('tocantins.json', 'r'))

print(df_tocantins.head())