def burbuja(lista) -> list:
    for pasada in range(len(lista)):
        for actual in range(0, len(lista)-pasada-1):
            if lista[actual] > lista[actual+1]:
                lista[actual], lista[actual+1] = lista[actual+1], lista[actual]
    return lista

lista = [2,8,5,3,9,4,1]
print("Lista base",lista)
print("Lista ordenada con burbuja",burbuja(lista))