lista = []

def menu():
    print('''
    Seleccione una opción del menu:
    1. Agregar
    2. Mostrar
    3. Remover x nombre
    4. Remover x posici?n
    5. Tamaño Lista
    6. Ordenar Ascendente
    7. Ordenar Descendente
    8. Consultar x posición
    9. Agregar en la posicion (x)
    0. Salir
    ''')
    op = int(input())
    return op

def main():
    while(True):
        processInput(menu())

def processInput(option):
    if(option == 1):
        agregarItem()
    elif(option == 2):
        mostrarLista()
    elif(option == 3):
        eliminarItem()
    elif(option == 4):
        eliminarItem(True)
    elif(option == 5):
        size()
    elif(option == 6):
        ordenar("ASC")
    elif(option == 7):
        ordenar("DESC")
    elif(option == 8):
        consultar()
    elif(option == 9):
        agregaPos()


def agregarItem():
    print("Digite el nuevo elemento")
    lista.append(input())
    print("El elemento fue agregado exitosamente")
    mostrarLista()

def mostrarLista():
    print("Asi va la lista")
    print(lista)

def eliminarItem(modoPosicion=False):
    mostrarLista()
    item = input()
    if(modoPosicion):
        if(lista.count(item) > 0):
            lista.remove(item)
        else:
            print("No se pudo eliminar el elemento")
    else:
        if(len(lista) > item):
            lista.pop(item)
        else:
            print("Indice fuera del rango")   

def size():
    print("Tamaño de la lista:", len(lista))

def ordenar(orden):
    mostrarLista()
    if(orden == "ASC"):
        lista.sort()
    elif(orden == "DESC"):
        lista.reverse()
    mostrarLista()

def consultar():
    print("Indice a consultar")
    i = int(input())
    if len(lista) > i:
        print(lista[i])
    else:
        print("Índice fuera de rango")

def agregaPos():
    i,elem = map(str, input("Posición y elemento: ").split())
    i = int(i)
    if len(lista) > 0 and i < len(lista):
        lista.insert(i, elem)
    else:
        print("No fue posible agregar el elemento. Verifique índice")
    mostrarLista()

main()