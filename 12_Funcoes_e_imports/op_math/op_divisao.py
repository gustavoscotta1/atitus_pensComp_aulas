def divisao(a: int, b: int) -> int | None:
    if b == 0:
        return None

    negativo = False
    if a < 0:
        a = -a
        negativo = not negativo
    if b < 0:
        b = -b
        negativo = not negativo

    resultado = 0
    while a >= b:
        a -= b
        resultado += 1

    if negativo:
        resultado = -resultado

    return resultado

def test_divisao():
    assert divisao(-10, 2) == -5
    assert divisao(10, -2) == -5
    assert divisao(10, 2) == 5
    assert divisao(10, 0) is None
