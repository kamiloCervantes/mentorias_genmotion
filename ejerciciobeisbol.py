""" Una empresa de videojuegos requiere que realice un programa que permita 
jugar beisbol desde la consola. Usando mensajes en la consola el jugador
podrá interactuar con el juego. Tener en cuenta que el jugador ocupará 
la posición del bateador, el cual deberá indicar en cada lanzamiento 
hacia que direccion desea hacer el bateo y la potencia de 1 a 10.
El juego termina cuando el jugador alcance 3 outs. El jugador tambien 
puede ocupar las bases y anotar carreras, incluso hacer home run.
El jugador no podrá robar bases y no recibirá outs por las bases.
En los lanzamientos se decidirá al azar lo que sucede con el bateo:
Sea X un numero aleatorio entero entre 0 y 100, 
- se tiene que si el numero esta entre 0 y 15 corresponderia a una bola
- si esta entre 16 y 65, seria strike 
- si esta entre 66 y 100 seria un bateo. 
Igualmente en caso de un bateo se decidirá lo que ocurre con el bateo con un valor
al azar. 
Sea Y un numero aleatorio entero entre 0 y 100, se tiene que:
- si el bateo fue a la izquierda o a la derecha
    - si el numero esta entre 90 y 100 y la potencia esta entre 9 y 10, se genera un 
    homerun y todas las bases ocupadas se convierten en carreras. 
    - Si el numero esta entre 70 y 89 y la potencia es mayor a 7 se genera un fly el 
    cual se convierte en out inmediatamente y las bases ocupadas no avanzarian a la 
    siguiente base.
    - Si el numero esta entre 45 y 69 y la potencia es mayor a 6 se genera un foul.
    *Recordar que un foul genera un strike cuando van al menos 2 strikes. En el tercer 
    strike, los fouls no generan strike.*
    - Si el numero esta entre 20 y 44 y la potencia es mayor a 4 se genera un hit. 
    *El hit no generara out en ningun caso y ocupara una nueva base. Si todas las bases 
    estan ocupadas genera carrera y se mantienen las bases ocupadas*. 
    - Si el numero esta entre 0 y 20 y la potencia es hasta 3 se genera un hit corto. 
    Tiene el mismo efecto que el hit. 
    - En el resto de casos,se genera un foul. 
- Si el bateo es al centro 
    - Si el numero aleatorio es mayor que 90 y la potencia es igual a 10 se tiene un 
    home run.
    - Si el numero esta entre 60 y 90 y la potencia es mayor a 7 se genera un fly con
    out automatico.
    - Si el numero esta entre 30 y 60 y la potencia es mayor a 5,
    se genera un hit. 
    - Si el numero esta entre 20 y 30 y la potencia es menor a 4 se genera un hit corto. 
    - En el resto de los casos se genera un foul. """

import random

outs = 0
balls = 0
strikes = 0
hits = 0
flies = 0
homeruns = 0
fouls = 0
bases = 0
runs = 0


def homerun():
    global balls
    global strikes
    global homeruns
    global bases
    global runs
    print("---Impresionante! Un homerun!!---")
    print("Felicidades!! Anotas",bases,"nuevas carreras!!!")
    runs = runs + bases
    bases = 0
    strikes = 0
    balls = 0
    homeruns = homeruns + 1

def fly():
    global outs
    global balls
    global strikes
    global flies
    print("---Se va y se va y se va y viene, oh no! es un fly, atrapado por el receptor---")
    outs = outs+1
    strikes = 0
    balls = 0
    flies = flies + 1

def foul():
    global strikes
    global fouls
    print("--- Oh no es un foul por muy poco!! ---")
    fouls = fouls + 1
    if(strikes < 3):
        strikes = strikes + 1

def hit():
    global balls
    global strikes
    global hits
    global bases
    bases = bases + 1
    strikes = 0
    balls = 0
    hits = hits + 1

def main():
    global outs
    global balls
    global strikes
    global hits
    global flies
    global homeruns
    global fouls
    global bases
    global runs
    while outs < 3:
        bateo = False
        error = False
        direccion = 0
        potencia = 0
          # movimiento de estadisticas
        if(balls == 4):
            balls = 0
            strikes = 0
            bases = bases+1
        if(strikes == 3):
            strikes = 0
            balls = 0
            outs = outs+1
        if(bases == 4):
            bases = 3
            runs = runs + 1
        if(outs == 3):
            break
        # lanzar pelota
        print("-------Estadisticas--------")
        print("Balls:", balls)
        print("Strikes:", strikes)
        print("Outs:", outs)
        print("Hits:", hits)
        print("Fly:", flies)
        print("Homeruns:", homeruns)
        print("Fouls:", fouls)
        print("Bases:", bases)
        print("Runs:", runs)
        print("---------------------------\n")
        print("Preparando lanzamiento de pelota")
        print("Pitcher lanza la pelota")
        print("Preparando swing de bateo")
        print("Seleccione la direccion del bateo\n1. Izquierda\n2. Centro\n3. Derecha")
        direccion = int(input())
        print("Indique la potencia del bateo (1-10)")
        potencia = int(input())
        # mostrar resultado de lanzamiento 
        X = random.randint(0,100)
        print(X)
        if(X > 0 and X <= 15):
            balls = balls +1
            print("Arbitro dice: Ball!")
            continue
        elif(X > 15 and X <= 65):
            strikes = strikes+1        
            print("Arbitro dice: Strike!")
            continue
        elif(X>65 and X <= 100):
            bateo = True
            print("---Increible! Logró batear!---")
    
        # mostrar resultado bateo    
        Y = random.randint(0,100)
        if(potencia >= 1 and potencia <= 10):
            if(direccion == 1 or direccion == 3):
                if((Y >= 90 and Y <= 100) and potencia >= 9):
                    homerun()
                elif((Y >= 70 and Y <= 89) and potencia >= 7):
                    fly()
                elif((Y >= 45 and Y <= 69) and potencia >= 6):
                    foul()
                elif((Y >= 20 and Y <= 44) and potencia >= 4):
                    print("---Excelente!! Un hit potente!! Safe en una nueva base!!---")
                    hit()      
                elif((Y >= 0 and Y <= 20) and potencia <= 3):
                    print("---Que gran tecnica!! Un hit corto!! Safe en una nueva base!!---")
                    hit()
                else:
                    foul()
            elif (direccion == 2):
                if((Y >= 90 and Y <= 100) and potencia == 10):
                    homerun()
                elif((Y >= 60 and Y <= 90) and potencia >= 7):
                    fly()
                elif((Y >= 30 and Y <= 60) and potencia >= 5):
                    print("---Excelente!! Un hit potente!! Safe en una nueva base!!---")
                    hit()
                elif((Y >= 20 and Y <= 30) and potencia <= 4):
                    print("---Que gran tecnica!! Un hit corto!! Safe en una nueva base!!---")
                    hit()
                else:
                    foul()
            else:
                error = True
        else:
            error = True
        # en caso de error reiniciar lanzamiento
        if(error):
            print("Hubo un error al ingresar los datos, se anula el lanzamiento")
            continue

      
    
main()
