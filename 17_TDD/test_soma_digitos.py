def soma_str(param: str) -> int:
    total = 0
    for char in param:
        if char.isdigit():
            total += int(char)
    return total


def test_soma_str():
    assert soma_str("") == 0
    assert soma_str("a") == 0
    assert soma_str("4") == 4
    assert soma_str("5ab6") == 11
    assert soma_str("3 -4 z5") == 12
    assert soma_str("11a2z3") == 7
