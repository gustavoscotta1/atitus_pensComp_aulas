def horoscopo(mes):
    if mes <= 0 or mes > 12:
        return "Valor inválido"
    if mes > 0 and mes <= 3:
        return "Você é do signo de Python"        
    if mes >= 4 and mes <= 6:
        return "Você é do signo de Java"
    if mes >= 7 and mes <= 9:
        return "Você é do signo de PHP"
    if mes >= 10 and mes <= 12:
        return "Você é do signo de TypeScript"   

def test(): 

    assert horoscopo(1) == "Você é do signo de Python"
    assert horoscopo(2) == "Você é do signo de Python"

    assert horoscopo(4) == "Você é do signo de Java"
    assert horoscopo(6) == "Você é do signo de Java"

    assert horoscopo(7) == "Você é do signo de PHP"
    assert horoscopo(9) == "Você é do signo de PHP"

    assert horoscopo(10) == "Você é do signo de TypeScript"
    assert horoscopo(12) == "Você é do signo de TypeScript"

    assert horoscopo(-1) == "Valor iválido"
    assert horoscopo(0) == "Valor iválido"
    assert horoscopo(13) == "Valor iválido"

print(horoscopo(5))
print(horoscopo(12))
print(horoscopo(3))
print(horoscopo(15))
print(horoscopo(-2))
