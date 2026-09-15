def insercion(lista) -> list:
    for actual in range(1, len(lista)):
        valor = lista[actual]
        atras = actual - 1
        while atras >= 0 and valor < lista[atras]:
            lista[atras + 1] = lista[atras]
            atras -= 1
        lista[atras + 1] = valor
    return lista

lista = [2,8,5,3,9,4,1]
print("Lista base", lista)
print("Lista ordenada con insercion", insercion(lista))