matriz_acidez = []
matriz_oxido_fosforo = []
zonas = 3
for i in range(zonas):
    print("Ingrese los valores de acidez")
    entrada = input()
    lista = entrada.split(" ")
    matriz_acidez.append(lista)
print(matriz_acidez)

print(matriz_acidez[0][2])

for i in range(zonas):
    print("Ingrese los valores de oxido de fosforo")
    entrada = input()
    lista = entrada.split(" ")
    matriz_oxido_fosforo.append(lista)
print(matriz_oxido_fosforo)

print(matriz_oxido_fosforo[0][2])