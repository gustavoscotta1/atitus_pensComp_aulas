def encontra_duplicados(lista):
    lista_nova = []
    for number in lista:
        if number in lista_nova:
            return True
        lista_nova.append(number)
    return False

def test_encontra_duplicados():
    assert encontra_duplicados([]) == False
    assert encontra_duplicados([1]) == False
    assert encontra_duplicados([1, 2]) == False
    assert encontra_duplicados([1, 2, 3, 1]) == True
    assert encontra_duplicados([1, 2, 3, 3, 2, 1]) == True

def lista_duplicados(lista):
    lista_nova = []
    duplicados = []
    for number in lista:
        if number in lista_nova and number not in duplicados:
            duplicados.append(number)
        else:
            lista_nova.append(number)
    return duplicados

def test_lista_duplicados():
    assert lista_duplicados([]) == []
    assert lista_duplicados([1]) == []
    assert lista_duplicados([1, 2]) == []
    assert lista_duplicados([1, 2, 3, 1]) == [1]
    assert lista_duplicados([1, 2, 3, 3, 2, 1]) == [3, 2, 1]

def ordena_lista(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

def test():
    assert ordena_lista([]) == []
    assert ordena_lista([1]) == [1]
    assert ordena_lista([4, 3, 2, 2, 1, 0]) == [0, 1, 2, 2, 3, 4]
    assert ordena_lista([10, 0, -3, 42, 5, -6, 8, 91]) == [-6, -3, 0, 5, 8, 10, 42, 91]
