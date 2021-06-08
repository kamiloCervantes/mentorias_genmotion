lista_hemoglobina = [2.3, 4.3, 15.6, 7.5, 25.6]

promedio = 8
cont = 0
for i in range(len(lista_hemoglobina)):
    if(lista_hemoglobina[i] > promedio):
        cont = cont + 1

print(cont)