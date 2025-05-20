def ordena_lista(lista):
    for i in range (len(lista)):
        for j in range (len(lista)-1):
            if lista[j] > lista[j+1]
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista
                


def test():
    assert ordena_lista([]) == []
    assert ordena_lista([1]) == [1]
    assert ordena_lista([4, 3, 2, 2, 1, 0]) == [0, 1, 2, 2, 3, 4]
    assert ordena_lista([10, 0, -3, 42, 5, -6, 8, 91]) == [-6, -3, 0, 5, 8, 10, 42, 91]
