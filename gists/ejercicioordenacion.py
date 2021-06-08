listapuntajes = [-1, 30, 30, -1, 8]
listaetnias = ["a", "x", "b", "c", "z"]
listaresultado = []
contador_a = 0
max = 0
for i in range(len(listapuntajes)):
    if(listapuntajes[i] > max and listapuntajes[i] > 0):
        max = listapuntajes[i]

posicion = listapuntajes.index(max)
etnia = listaetnias[posicion]
listaresultado.append(etnia)

listaetniasordenadas = ["a", "b", "z"]
print(listaetniasordenadas[0], contador_a)