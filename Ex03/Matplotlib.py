import matplotlib.pyplot as plt
import numpy as np

np.random.seed(3)
x = 0.5 + np.arange(8)
mes = np.arange(12) + 1 # meses de 1 a 12
legendas = ['Creme Facial', 'Limpeza Facial', 'Pasta Dentaria', 'Sabonete', 'shampoo', 'Hidratante']

# quantidades de produtos vendidos por mês. As entradas são de Janeiro a Dezembro
creme_facial = np.array([ 2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900 ])
limpeza_facial = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
pasta_dentaria = np.array([ 5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400 ])
sabonete = np.array([ 9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400 ])
shampoo = np.array([ 1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800 ])
hidratante = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])

# Gráfico 1 - Total de produtos Vendidos por mês - Linha
fig, ax = plt.subplots()
ax.set_title("Total de Produtos Vendidos Mês a Mês")
ax.plot(mes, creme_facial + limpeza_facial + pasta_dentaria + sabonete + shampoo + hidratante)
plt.show()

# Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha
fig, ax = plt.subplots()
ax.set_title("Quantidade de Produtos Vendidos Mês a Mês")
ax.plot(mes, creme_facial)
ax.plot(mes, limpeza_facial)
ax.plot(mes, pasta_dentaria)
ax.plot(mes, sabonete)
ax.plot(mes, shampoo)
ax.plot(mes, hidratante)
ax.set_xticks(mes)
ax.set_xticklabels(mes)
ax.legend(labels=legendas)
plt.show()

# Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras
fig, ax = plt.subplots(figsize=(12, 6))
largura = 0.35
x = np.arange(len(mes))

ax.bar(x - largura/2, creme_facial, width=largura, label="Creme Facial")
ax.bar(x + largura/2, limpeza_facial, width=largura, label="Limpeza Facial")

ax.set_title("Comparativo de Vendas - Creme vs Limpeza Facial")
ax.set_xticks(x)
ax.set_xticklabels(mes)
ax.legend()
plt.show()

# Gráfico 4 - Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...)
bins = np.arange(1000, 15001, 1000)
plt.figure(figsize=(18, 7))
plt.hist(
    [creme_facial, limpeza_facial, pasta_dentaria, sabonete, shampoo, hidratante],
    bins=bins,
    label=['Creme Facial', 'Limpeza Facial', 'Pasta Dentaria', 'Sabonete', 'Shampoo', 'Hidratante']
)
plt.title("Histograma de Vendas - Meses por Faixa de Quantidade")
plt.xlabel("Faixa de quantidade vendida")
plt.ylabel("Quantidade de meses")
plt.xticks(bins)
plt.legend()
plt.show()

# Gráfico 5 - Pizza com % da quantidade produtos vendidos no ano em cada produto
fig, ax = plt.subplots(figsize=(8,8))
soma_produtos = [
    creme_facial.sum(),
    limpeza_facial.sum(),
    pasta_dentaria.sum(),
    sabonete.sum(),
    shampoo.sum(),
    hidratante.sum()
]
ax.pie(
    soma_produtos,
    labels=legendas,
    autopct='%1.1f%%',  # mostra as porcentagens com 1 casa decimal
    startangle=90,      # começa do topo (90 graus)
    wedgeprops={"edgecolor":"white"}  # borda branca separando as fatias
)
ax.set_title("Participação (%) de cada produto no total de vendas do ano")
plt.show()