def eh_bissexto(ano):
    if ano % 4 == 0:
        return True 
    else: 
        return False 


def proximo_bissexto(ano):
    if ano % 4 == 0:
        return ano 
    if ano % 4 == 1:
        return ano + (3)
    if ano % 4 == 2:
        return ano + (2)
    if ano % 4 == 3:
        return ano + (1)

def test(): 
    assert eh_bissexto(0)
    assert eh_bissexto(2020)
    assert eh_bissexto(2024)

    assert not eh_bissexto(1)
    assert not eh_bissexto(2022)
    assert not eh_bissexto(2023)

    assert proximo_bissexto(2024) == 2024
    assert proximo_bissexto(2025) == 2028
    assert proximo_bissexto(2029) == 2032
    assert proximo_bissexto(2020) == 2020

print(eh_bissexto(2020))
print(eh_bissexto(1907))
print(eh_bissexto(4560))
print(proximo_bissexto(2025))
print(proximo_bissexto(2022))
print(proximo_bissexto(2020))