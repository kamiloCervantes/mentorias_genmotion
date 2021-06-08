def actividad1(matriz):
    cuadrada = True
    for lista in matriz:
        if(len(lista) != len(matriz)):
            cuadrada = False        
    if(cuadrada):
        # imprimir diagonal
        diagonal_list = []
        for i in range(len(matriz)):
            diagonal_list.append(matriz[i][i])      
        print("La matriz es cuadrada")
        print(diagonal_list)
    else:
        print("La matriz no es cuadrada")

actividad1([[1,2,3],[4,5,6],[7,8,9]])
