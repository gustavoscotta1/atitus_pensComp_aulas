def calcula_classe_social(salarios, salario_minimo):
    if not salarios:
        return None  

    total_salarios = sum(salarios)
    quantidade_salarios = len(salarios)
    media = total_salarios / quantidade_salarios
    renda_em_salarios_minimos = media / salario_minimo

    if renda_em_salarios_minimos <= 1:
        return "E"
    elif renda_em_salarios_minimos <= 2:
        return "D"
    elif renda_em_salarios_minimos <= 4:
        return "C"
    elif renda_em_salarios_minimos <= 10:
        return "B"
    else:
        return "A"


def test():
    assert calcula_classe_social([], 1000) is None
    assert calcula_classe_social([1000], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([1000, 0], 900) == "E"
    assert calcula_classe_social([1000], 900) == "D"
    assert calcula_classe_social([10000, 15000], 1000) == "A"  
    assert calcula_classe_social([20000, 25000], 1000) == "A"
    assert calcula_classe_social([20000, 0, 0, 0, 0], 1000) == "C"