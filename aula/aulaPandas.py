import pandas as pd

caminho = r"H:\3A2 Python\industriasPY\aula\banco_teste - banco_teste - banco_teste - banco_teste.csv"

df = pd.read_csv(caminho, sep=";")


# print(df.head())

# print(df.dtypes)


df['pais'] = "Brasil"


print(df.head())