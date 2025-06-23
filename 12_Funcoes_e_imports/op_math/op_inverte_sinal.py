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

def inverte_sinal(a: int) -> int:
    return multiplicacao(a, -1)

def test_inverte_sinal():
    assert inverte_sinal(1) == -1
    assert inverte_sinal(-2) == 2

