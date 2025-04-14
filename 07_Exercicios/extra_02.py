def maior_numero(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

def menor_numero(lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def numeros_impares(lista):
    impares = []
    for numero in lista:
        if numero % 2 != 0:
            impares.append(numero)
    return impares

def numeros_positivo(lista):
    positivos = []
    for numero in lista:
        if numero >= 0:
            positivos.append(numero)
    return positivos

def numeros_negativos(lista):
    negativos = []
    for numero in lista:
        if numero < 0:
            negativos.append(numero)
    return negativos

def soma_numeros(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma


lista_1 = [10, 0, -3, 42, 5, -6, 8, 91]
lista_2 = [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
lista_3 = [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

def test():
    assert maior_numero(lista_1) == 91
    assert maior_numero(lista_2) == 95
    assert maior_numero(lista_3) == 92

    assert menor_numero(lista_1) == -6
    assert menor_numero(lista_2) == 2
    assert menor_numero(lista_3) == 5

    assert numeros_pares(lista_1) == [10, 0, 42, -6, 8]
    assert numeros_pares(lista_2) == [20, 2, 74, 22]
    assert numeros_pares(lista_3) == [92, 50, 28]

    assert numeros_impares(lista_1) == [-3, 5, 91]
    assert numeros_impares(lista_2) == [27, 19, 85, 3, 95, 11]
    assert numeros_impares(lista_3) == [45, 23, 17, 89, 57, 15, 5]

    assert numeros_positivo(lista_1) == [10, 0, 42, 5, 8, 91]
    assert numeros_positivo(lista_2) == [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
    assert numeros_positivo(lista_3) == [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

    assert numeros_negativos(lista_1) == [-3, -6]
    assert numeros_negativos(lista_2) == []
    assert numeros_negativos(lista_3) == []

    assert soma_numeros(lista_1) == 147
    assert soma_numeros(lista_2) == 358
    assert soma_numeros(lista_3) == 421
