def adicao(valor1: int, valor2: int) -> int:
    resultado = valor1

    if valor2 > 0:
        for _ in range(valor2):
            resultado += 1
    elif valor2 < 0:
        for _ in range(-valor2):
            resultado -= 1

    return resultado

def test_adicao():
    assert adicao(1, 2) == 3
    assert adicao(1, 0) == 1
    assert adicao(-1, -2) == -3

