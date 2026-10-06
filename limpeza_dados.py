import pandas as pd
df = pd.read_csv("data.csv")

print(df)
print("Linhas:", df.shape[0])
print("Colunas:", df.shape[1])
print("Nome das Colunas:", df.columns.tolist())

print("Valores Nulos:", df.isna().sum())

print("Colunas com valores ausentes:")
print(df.isna().sum()[df.isna().sum() > 0])

df.fillna({"Calories": 300}, inplace=True)

print("DataFrame depois da limpeza:")
print(df.to_string())

print("Valores Nulos depois da limpeza:")
print(df.isna().sum())