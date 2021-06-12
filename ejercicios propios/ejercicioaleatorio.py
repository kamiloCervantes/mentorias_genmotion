import random
import math

def cargarDatos():
    lista = []
    data=""
    try:
        data = open('participantes.cfg', 'r')
        for item in data.readlines():
            lista.append(item.replace('\n',''))                       
    except FileNotFoundError:
        print('Archivo no encontrado')
    finally:
        data.close()
    return lista


def main():
    lista = cargarDatos()
    num = random.randint(1,100)
    vueltas = math.ceil(num/len(lista))
    for i in range(vueltas):
        for j in range(len(lista)):            
            num -= 1
            if(num == 0):
                print('>',lista[j])
                break
            print('-',lista[j])

main()


