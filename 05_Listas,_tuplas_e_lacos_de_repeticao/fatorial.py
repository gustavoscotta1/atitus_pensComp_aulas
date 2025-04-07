def fatorial(numero):
    if numero < 0:
        return None  
    resultado = 1
    i = 1
    while i <= numero:
        resultado *= i
        i += 1
    return resultado
    


assert fatorial(0) == 1
assert fatorial(1) == 1
assert fatorial(2) == 2
assert fatorial(3) == 6
assert fatorial(4) == 24
assert fatorial(5) == 120
assert fatorial(-1) is None
