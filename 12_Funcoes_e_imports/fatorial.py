def fatorial_rec(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * fatorial_rec(n - 1)

def fatorial_non_rec(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def test_fatorial():
    assert fatorial_rec(-1) is None
    assert fatorial_rec(0) == 1
    assert fatorial_rec(1) == 1
    assert fatorial_rec(2) == 2
    assert fatorial_rec(3) == 6
    assert fatorial_rec(4) == 24
    assert fatorial_rec(5) == 120

    assert fatorial_non_rec(-1) is None
    assert fatorial_non_rec(0) == 1
    assert fatorial_non_rec(1) == 1
    assert fatorial_non_rec(2) == 2
    assert fatorial_non_rec(3) == 6
    assert fatorial_non_rec(4) == 24
    assert fatorial_non_rec(5) == 120

