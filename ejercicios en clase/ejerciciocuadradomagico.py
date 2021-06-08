
def cuadradoMagicoGet(matriz):
    valor = 0
    for n in matriz[0]:
        valor = valor + n
    cuadradoMagico = True
    for fila in matriz:
        sumafilas = 0
        for i in range(len(fila)):
           sumafilas = sumafilas + fila[i]
        if(sumafilas != valor):
            cuadradoMagico = False
    
    for a in range(len(matriz)):
        sumacolumnas = 0
        for b in range(len(matriz)):
            sumacolumnas = sumacolumnas + matriz[b][a]
    if(sumacolumnas != valor):
        cuadradoMagico = False
    
    sumadiagonal1 = 0    
    for k in range(len(matriz)):        
        sumadiagonal1 = sumadiagonal1 + matriz[k][k]
    if(sumadiagonal1 != valor):
        cuadradoMagico = False

    sumadiagonal2 = 0    
    for g in range(len(matriz)):
        sumadiagonal2 = sumadiagonal2 + matriz[g][(len(matriz)-1-g)]
    if(sumadiagonal2 != valor):
        cuadradoMagico = False
    if(cuadradoMagico):
        print("Es un cuadrado magico")
    else:
        print("No es cuadrado magico")
cuadradoMagicoGet( [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]])