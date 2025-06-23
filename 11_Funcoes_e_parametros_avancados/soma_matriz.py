def soma_matriz(matriz, alvo):
    lista_par = []
    for linha in matriz:
        for numero in linha:
            if numero % 2 == 0:
                lista_par.append(numero)
            else:
                pass
            
    total = 0
    for soma in lista_par:
        total += soma

    if total == alvo:
        return True
    else:
        return False

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def test_soma_matriz():
    assert soma_matriz(matriz, 20)
    assert not soma_matriz(matriz, 18)
    assert not soma_matriz(matriz, 21)
    assert not soma_matriz(matriz, 22)