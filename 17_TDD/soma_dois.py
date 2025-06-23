def soma_dois(lista: list, alvo: int) -> list | None:
    if len(lista) < 2:
        return None
    indice_map = {}
    for i, num in enumerate(lista):
        complemento = alvo - num
        if complemento in indice_map:
            return [indice_map[complemento], i]
        indice_map[num] = i
    return None


def test_soma_dois():
    assert soma_dois([2, 7, 11, 15], 9) == [0, 1]
    assert soma_dois([3, 2, 4], 6) == [1, 2]
    assert soma_dois([3, 3], 6) == [0, 1]
    assert soma_dois([], 6) is None
    assert soma_dois([1], 6) is None
    assert soma_dois([1, 2], 6) is None
