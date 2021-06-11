# una matriz es una lista de listas
# se inicializa igual que las listas
matriz = []

# se le pueden añadir listas
lista1 = [1,3,5,6,7]
matriz.append(lista1)
lista2 = [2,5,6,7,8]
matriz.append(lista2)
# [[1, 3, 5, 6, 7], [2, 5, 6, 7, 8]]
print(matriz)
# para acceder a un elemento de la matriz se le deben pasar
# dos datos, la fila y columna.
# Ejemplo. Mostrar el tercer elemento de la segunda lista
# Nota: el conteo de las posiciones inicia en 0
# 6
print(matriz[1][2])
