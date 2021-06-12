lista = [["a", 3], ["x", 5], ["y", 8], ["z", 3], ["m", 4]]
listat = (("a", 3), ("x", 5), ("y", 8), ("z", 3), ("m", 4))

lista.sort(key=lambda item:item[1])
print(lista)