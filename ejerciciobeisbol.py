Una empresa de videojuegos requiere que realice un programa que permita 
jugar beisbol desde la consola. Usando mensajes en la consola el jugador
podrá interactuar con el juego. Tener en cuenta que el jugador ocupará 
la posición del bateador, el cual deberá indicar en cada lanzamiento 
hacia que direccion desea hacer el bateo y la potencia de 1 a 10.
El juego termina cuando el jugador alcance 3 outs. El jugador tambien 
puede ocupar las bases y anotar carreras, incluso hacer home run.
El jugador no podrá robar bases y no recibirá outs por las bases.
En los lanzamientos se decidirá al azar lo que sucede con el bateo:
Sea x un numero aleatorio entero entre 0 y 100, se tiene que si el
numero esta entre 0 y 15 corresponderia a una bola, si esta entre 16 y 65,
seria strike y si esta entre 66 y 100 seria un bateo. Igualmente en
caso de un bateo se decidirá lo que ocurre con el bateo con un valor
al azar. 
Sea y un numero aleatorio entero entre 0 y 100, se tiene que si el 
bateo fue a la izquierda o a la derecha y el numero esta entre 90 y 100
y la potencia esta entre 9 y 10, se genera un homerun y todas las 
bases ocupadas se convierten en carreras. Si el numero esta entre 70 y 89
y la potencia es mayor a 7 y el bateo fue a la izquierda o a la derecha
se genera un fly el cual se convierte en out inmediatamente y las 
bases ocupadas no avanzarian a la siguiente base.
Si el numero esta entre 45 y 69 y el bateo fue a la izquierda o derecha y 
la potencia es mayor a 6 se genera un foul. Recordar que un foul genera un
strike cuando van al menos 2 strikes. En el tercer strike, los fouls
no generan strike. Si el numero esta entre 20 y 44 y la potencia es mayor a
4, y el bateo es a la izquierda o a la derecha se genera un hit. El hit no 
generara out en ningun caso y ocupara una nueva base. Si todas las bases 
estan ocupadas genera carrera y se mantienen las bases ocupadas. 
Si el numero esta entre 0 y 20 y la potencia es hasta 3 se genera un 
hit corto. Tiene el mismo efecto que el hit. En el resto de casos,
se genera un foul. 
Si el bateo es al centro y el numero aleatorio es mayor que 90 y la potencia 
es igual a 10 se tiene un home run. Si es al centro y el numero esta entre
60 y 90 y la potencia es mayor a 7 se genera un fly con out automatico.
Si es al centro y el numero esta entre 30 y 60 y la potencia es mayor a 5,
se genera un hit. Si es al centro y el numero esta entre 20 y 30 y la potencia
es menor a 4 se genera un hit corto. En el resto de los casos se genera
un foul.