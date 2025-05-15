def eh_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    i = 2
    while numero % i != 0:
        i = i + 1
    if i == numero:
        return True
    return False

def test(): 
    assert not eh_primo(-1)
    assert not eh_primo(0)
    assert not eh_primo(1)
    assert eh_primo(2)
    assert eh_primo(3)
    assert not eh_primo(4)
    assert eh_primo(5)
