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

def test_multiplicacao():
    assert multiplicacao(-10, 2) == -20
    assert multiplicacao(10, -2) == -20
    assert multiplicacao(10, 2) == 20
    assert multiplicacao(10, 0) == 0
