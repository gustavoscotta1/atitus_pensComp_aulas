def subtracao(valor1: int, valor2: int) -> int:
    # subtracao(a, b): não pode usar o símbolo ‘-’
    pass


assert subtracao(-10, 2) == -12
assert subtracao(10, -2) == 12
assert subtracao(-10, -2) == -14
assert subtracao(10, 2) == 8
assert subtracao(10, 0) == 10

def subtracao(valor1: int, valor2: int) -> int:
    def inverte_sinal(a: int) -> int:
        return multiplicacao(a, -1)
    
    def multiplicacao(a: int, b: int) -> int:
        resultado = 0
        negativo = False
        if a < 0:
            a = -a
            negativo = not negativo
        if b < 0:
            b = -b
            negativo = not negativo
        for _ in range(b):
            resultado += a
        if negativo:
            resultado = -resultado
        return resultado

    return valor1 + inverte_sinal(valor2)

def test_subtracao():
    assert subtracao(-10, 2) == -12
    assert subtracao(10, -2) == 12
    assert subtracao(-10, -2) == -14
    assert subtracao(10, 2) == 8
    assert subtracao(10, 0) == 10

