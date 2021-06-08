# A partir del ejercicio anterior, modificar el programa de tal forma que se solicite el numero de boletas a 
# vender y los numeros de sillas deseados, finalmente el programa debe mostrar el valor total de la compra
# teniendo en cuenta que los valores deben ser acorde al tipo de silla solicitado.

#pedimos el numero de boletas al usuario
print("Ingrese el numero de boletas que desea")
numboletas = int(input())
#variable controladora del ciclo (Se incrementa en 1 en cada repeticion)
contador = 1
# en esta variable se va acumulando el total a pagar por concepto de boletas
totalpagoboletas = 0
while(contador<=numboletas):
    print("----- Boleta",contador,"------")
    # Se ejecuta indefinidamente hasta que encuentre una respuesta correcta
    while(True):
        #pedimos el numero de la silla al usuario
        print("Ingrese el numero de la silla que desea")
        numsilla = int(input())
        #verificamos que la silla sea mayor que 0
        if(numsilla > 0):
            #dependiendo del tipo de silla se le incrementa al valor el precio que corresponde
            if(numsilla >= 1 and numsilla <= 20):
                totalpagoboletas = totalpagoboletas + 5000
                break
            elif(numsilla >= 21 and numsilla <= 40):
                totalpagoboletas = totalpagoboletas + 7000
                break
            elif(numsilla >= 41 and numsilla <=50):
                totalpagoboletas = totalpagoboletas + 10000
                break
            else:
                print("Error: La silla no existe")    
        else:
            print("Error: La silla no existe")
    contador = contador+1

# se imprime el valor total de las boletas
print("El valor de las boletas es ", totalpagoboletas)
