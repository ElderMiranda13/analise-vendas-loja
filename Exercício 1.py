import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly as px 


#importar os dados de vendas.
df = pd.read_csv("vendas_loja.csv")
print(df) 

#calcular receita total por produto.
caminho_pasta = r'C:\Users\Elder\Desktop\Meu projeto'

# Cria um DataFrame vazio pra juntar todos os dados
df_total = pd.DataFrame()

# Loop pelos arquivos dentro da pasta
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith(".csv"):
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        df = pd.read_csv(caminho_completo)
        df_total = pd.concat([df_total, df], ignore_index=True)

# Verifica se as colunas existem
if "Produto" in df_total.columns and "Total" in df_total.columns:
    receita_por_produto = df_total.groupby("Produto")["Total"].sum()
    print("\n📊 Receita total por produto:")
    print(receita_por_produto)
else:
    print("❌ As colunas 'Produto' e 'Total' não foram encontradas.")
    print("Colunas disponíveis:", df_total.columns.tolist())

    
#produto mais vendido.
df = pd.read_csv(r"C:\Users\Elder\Desktop\Meu projeto\vendas_loja.csv")

# Agrupa por produto e soma as quantidades vendidas
quantidade_vendida = df.groupby("Produto")["Quantidade"].sum()

# Ordena do maior para o menor
quantidade_ordenada = quantidade_vendida.sort_values(ascending=False)

# Exibe o mais vendido
mais_vendido = quantidade_ordenada.idxmax()  # Retorna o nome do produto
quantidade_maxima = quantidade_ordenada.max()  # Retorna a quantidade

print(f"Produto mais vendido: {mais_vendido} ({quantidade_maxima} unidades)")


#receita total por mês, usando datas.

df = pd.read_csv(r"C:\Users\Elder\Desktop\Meu Projeto\vendas_loja.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["AnoMes"] = df["Data"].dt.to_period("M")
receita_por_mes = df.groupby("AnoMes")["Total"].sum()
print(receita_por_mes)
    
#usar gráfico de barras para, mostrar receitas por produto.
df = pd.read_csv(r"C:\Users\Elder\Desktop\Meu projeto\vendas_loja.csv")
receita_produto = df.groupby("Produto")["Total"].sum()
plt.figure(1)
receita_produto.plot(kind="bar", color="skyblue", title="Receita por produto")
plt.xlabel("Produto")
plt.ylabel("Receita (R$)")
plt.tight_layout()



#fazer um gráfico de linha, mostrando a evolução mensal das vendas.
df = pd.read_csv(r"C:\Users\Elder\Desktop\Meu Projeto\vendas_loja.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["AnoMes"] = df["Data"].dt.to_period("M")
receita_mensal = df.groupby("AnoMes")["Total"].sum()
plt.figure(2)
receita_mensal.plot(kind="line", marker="o", color="Green", title="Evolução Mensal das Vendas")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.grid(True)
plt.tight_layout()

#mostrar os dois gráficos simultaneamente.
plt.show()




