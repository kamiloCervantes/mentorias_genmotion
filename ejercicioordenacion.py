listapuntajes = [20, 30, 10, -1, 8]
listaetnias = ["a", "x", "b", "a", "z"]

max = 0
for i in range(len(listapuntajes)):
    if(listapuntajes[i] > max and listapuntajes[i] > 0):
        max = listapuntajes[i]

posicion = listapuntajes.index(max)
etnia = listaetnias[posicion]