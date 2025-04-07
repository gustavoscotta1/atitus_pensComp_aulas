def somatorio(numero):
    if numero <= -1:
        return None
    resultado = 0
    contador = 1
    while contador <= numero:
        resultado = resultado + contador
        contador = contador + 1
    return resultado

def test():
    assert somatorio(-1) is None
    assert somatorio(0) == 0
    assert somatorio(1) == 1
    assert somatorio(2) == 3
    assert somatorio(3) == 6
    assert somatorio(4) == 10
    assert somatorio(5) == 15
    assert somatorio(6) == 21
    assert somatorio(7) == 28
    assert somatorio(8) == 36
    assert somatorio(9) == 45