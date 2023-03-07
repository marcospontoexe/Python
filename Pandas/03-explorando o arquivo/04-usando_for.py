import pandas as pd

df = pd.read_excel("nomes.xlsx")
for i, linha in df.head(10).iterrows():
    print(f"índice {i} --> {linha['FirstName']}")