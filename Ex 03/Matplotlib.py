import matplotlib.pyplot as plt
import numpy as np

mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# quantidades de produtos vendidos por mês. As entradas são de Janeiro a Dezembro
creme_facial = np.array([ 2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900 ])
limpeza_facial = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
pasta_dentaria = np.array([ 5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400 ])
sabonete = np.array([ 9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400 ])
shampoo = np.array([ 1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800 ])
hidratante = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])

# Gráfico 1 - Total de produtos Vendidos por mês - Linha
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)
ax.set_title("Total de Produtos Vendidos Por Mês")
ax.set_ylabel("Vendas Por Mês")

ax.plot(mes, creme_facial + limpeza_facial + pasta_dentaria + sabonete + shampoo + hidratante, color="red")
ax.set_xticks(mes)

fig.show()

# Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha
fig, ax = plt.subplots()
fig.set_size_inches(15, 6)
ax.set_title("Vendas de Produtos Mensal")
ax.set_ylabel("Valores Vendidos")
ax.set_xlabel("Mês")

ax.set_xticks(mes)
ax.plot(mes, creme_facial, label="Creme Facial")
ax.plot(mes, limpeza_facial, label="Limpeza Facial")
ax.plot(mes, pasta_dentaria, label="Pasta Dentaria")
ax.plot(mes, sabonete, label="Sabonete")
ax.plot(mes, shampoo, label="Shampoo")
ax.plot(mes, hidratante, label="Hidratante")
ax.legend()

fig.show()

# Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras

largura = np.arange(1, 13)

fig, ax = plt.subplots()
fig.set_size_inches(15, 8)
ax.set_xticks(mes)

largura_da_barra = 0.3

ax.bar(largura - largura_da_barra/2, creme_facial, largura_da_barra, label="Creme Facial")
ax.bar(largura + largura_da_barra/2, limpeza_facial, largura_da_barra, label="Limpeza Facial")

ax.set_ylabel("Quantidade de Venda")
ax.set_xlabel("Mês")
ax.set_title("Comparativo de Creme Facial com Limpeza Facial Mensal")

ax.legend()
plt.show()

# Gráfico 4 - Stack plot com o total de produtos vendidos a cada mês com todos os produtos

fig, ax = plt.subplots()
fig.set_size_inches(15, 7)

ax.set_title("Total de Produtos Vendidos Mensalmente")
ax.set_ylabel("Valores de Venda")
ax.set_xlabel("Mês")
ax.set_xticks(mes)

ax.stackplot(mes, [creme_facial, limpeza_facial, pasta_dentaria, sabonete, shampoo, hidratante], labels=["Creme Facial", "Limpeza Facial", "Pasta Dentaria", "Sabonete", "Shampoo", "Hidratante"])
ax.legend()
plt.show()

# Gráfico 5 - Pizza com % da quantidade produtos vendidos no ano em cada produto

fig, ax = plt.subplots()
ax.set_title("Venda de Produtos Anual Por Categoria")

y = [np.sum(creme_facial), np.sum(limpeza_facial), np.sum(pasta_dentaria), np.sum(sabonete), np.sum(shampoo), np.sum(hidratante)]
textos = ["Creme Facial", "Limpeza Facial", "Pasta Dentaria", "Sabonete", "Shampoo", "Hidratante"]

ax.pie(y, labels=textos, autopct='%1.1f%%')
plt.show()