import numpy as np

temperaturas = np.array([2.5, 3.2, 5.1, 6.3, 7.0, 8.1, 10.5, 9.8, 8.5, 7.3,
    6.2, 5.1, 4.5, 3.8, 5.6, 6.7, 7.2, 8.3, 10.1, 9.4,
    8.2, 7.0, 6.3, 5.4, 4.7, 3.9, 5.8, 6.9, 7.4, 8.5,
    10.3, 9.6, 8.4, 7.2, 6.5, 5.6, 4.9, 4.1, 5.9, 7.0,
    7.5, 8.6, 10.4, 9.7, 8.5, 7.3, 6.6, 5.7, 5.0, 4.2,
    6.0, 7.1, 7.6, 8.7, 10.6, 9.9, 8.7, 7.5, 6.8, 5.9,
    5.2, 4.4, 6.1, 7.2, 7.7, 8.8, 10.7, 10.0, 8.8, 7.6,
    6.9, 6.0, 5.3, 4.5, 6.2, 7.3, 7.8, 8.9, 10.8, 10.2,
    9.0, 7.8, 7.1, 6.2, 5.5, 4.7, 6.3, 7.4, 7.9, 9.0,
    10.9, 10.3, 9.1, 7.9, 7.2, 6.3, 5.6, 4.8, 6.4, 7.5])

temp_dia_quente = 0
temp_dia_frio = 0
count_dia = 1

media_temperaturas = np.mean(temperaturas)

print("A média do array é " + str(round(media_temperaturas, 3)))

mediana_temperaturas = np.median(temperaturas)
print("\nA temperatura mediana é " + str(mediana_temperaturas))

desvio_padrao_temperaturas = np.std(temperaturas)
print("O\n desvio de padrão é " + str(round(desvio_padrao_temperaturas)))

for temp in temperaturas:
    if temp < 5:
        print("Dia " + str(count_dia) + " foi frio com temperatura de " + str(temp) + " graus celsius")
    if temp >= 5 and temp <= 15:
        print("Dia " + str(count_dia) + " foi moderado com temperatura de " + str(temp) + " graus celsius")
    if temp > 15:
        print("Dia " + str(count_dia) + " foi quente com temperatura de " + str(temp) + " graus celsius")
    count_dia = count_dia + 1

for i in range(1, len(temperaturas)):
    if temperaturas[i] > temp_dia_quente:
        temp_dia_quente = i
    elif temp_dia_quente == 0:
        temp_dia_quente = 1

for i in range(1, len(temperaturas)):
    if temperaturas[i] < temp_dia_frio:
        temp_dia_frio = i
    elif temp_dia_frio == 0:
        temp_dia_frio = 1

print("\nA temperatura mais alta registrada foi no dia " + str(temp_dia_quente) + " marcando " + str(np.max(temperaturas)))
print("A temperatura mais fria registrada foi no dia " + str(temp_dia_frio) + " marcando " + str(np.min(temperaturas)))