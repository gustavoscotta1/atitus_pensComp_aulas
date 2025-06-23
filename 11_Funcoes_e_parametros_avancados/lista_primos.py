def eh_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    i = 2
    while numero % i != 0:
        i = i + 1
    if i == numero:
        return True
    return False

def lista_primos(numero: int) -> list:
    lista_primos = []
    for j in range(numero + 1): 
        if eh_primo(j): 
            lista_primos.append(j)
    return lista_primos


def test_lista_primos():
    assert lista_primos(10) == [2, 3, 5, 7]
    assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
    assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


