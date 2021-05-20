# diseñe y desarrolle un programa para un cine que tiene una sala con 50 sillas donde las primeras 20 sillas
# se encuentran en la clase general, las segundas 20 sillas en la clase ejecutiva y las 10 sillas restantes
# en la zona vip. Los precios de las boletas son para clase general: $5000, para clase ejecutiva: $7000, 
# para clase vip: $10000. El objetivo del programa es presentar el costo de las boletas de acuerdo al numero
# de la silla a comprar.
# Ejemplo entrada   |   Ejemplo salida
# 15                    Clase general: $5000
# 32                    Clase ejecutiva: $7000
# 48                    Clase VIP: $10000
# 70                    Error: La silla no existe


#pedimos el numero de la silla al usuario
print("Ingrese el numero de la silla que desea")
numsilla = int(input())
#verificamos que la silla sea mayor que 0
if(numsilla > 0):
    if(numsilla >= 1 and numsilla <= 20):
        print("Clase general: $5000")
    elif(numsilla >= 21 and numsilla <= 40):
        print("Clase ejecutiva: $7000")
    elif(numsilla >= 41 and numsilla <=50):
        print("Clase VIP: $10000")
    else:
        print("Error: La silla no existe")    
else:
    print("Error: La silla no existe")