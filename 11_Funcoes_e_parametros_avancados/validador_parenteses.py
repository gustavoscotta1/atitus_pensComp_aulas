def validador_parenteses(entrada: str) -> bool:
    parenteses_a = ''
    parenteses_b = ''

    for x in entrada:
        if x == '(':
            parenteses_a += x
        else:
            parenteses_b += x

    if len(parenteses_a) == len(parenteses_b):
        return True
    else:
        return False


def test():# Valores válidos
    assert validador_parenteses("()")
    assert validador_parenteses("()()")
    assert validador_parenteses("(())")
    assert validador_parenteses("(()()())")
    assert validador_parenteses("(((())()))")

def test():# Valores inválidos
    assert validador_parenteses(")")
    assert validador_parenteses("(")
    assert validador_parenteses("()(")
    assert validador_parenteses("()()())")
    assert validador_parenteses("(((())())")