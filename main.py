import pandas as pd 
df = pd.read_csv("data.csv")
print(df)
print("Linhas:", df.shape[0])
print("Colunas:", df.shape[1])
print("Nome das Colunas:", df.columns.tolist())

print("Valores Nulos:", df.isna())
print("Soma dos Valores Nulos:", df.isna().sum())

new_df = df.dropna()
print("DataFrame sem Valores Nulos:", new_df.to_string())

df.dropna(inplace=True)
print(df.to_string())
print(df.isna().sum())

df.fillna(300, inplace=True)
print(df.to_string())
print(df.isna().sum())

df.fillna({"Calories": 350}, inplace=True)
print(df.to_string())
print(df.isna().sum())

df = pd.read_csv("data.csv")
df_dropna = df.dropna()
print("Versão com dropna:", df_dropna.to_string())

df = pd.read_csv("data.csv")
df_fillna = df.fillna({"Calories": 300})
print("Versão com fillna:", df_fillna.to_string())

print(df.isna().sum())
df.fillna({"Calories": 300}, inplace=True)
print(df.isna().sum())

df = pd.read_csv("data.csv")
print(df.isna().sum())
df.fillna({"Calories": 300}, inplace=True)
print(df.to_string())
print(df.isna().sum())