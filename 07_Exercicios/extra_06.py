def valor_pgto(valor, forma_pgto):
    if forma_pgto == 1:  # PIX
        return valor * 0.85  # 15% de desconto
    elif forma_pgto == 2:  # À vista
        return valor * 0.90  # 10% de desconto
    elif forma_pgto == 3:  # Parcelado 2x sem juros
        return valor
    elif forma_pgto == 4:  # Parcelado 3x ou mais com juros
        return valor * 1.10  # 10% de acréscimo
    else:
        return None  # opção inválida


def test():
    assert abs(valor_pgto(100, 1) - 85) < 1e-6
    assert abs(valor_pgto(100, 2) - 90) < 1e-6
    assert abs(valor_pgto(100, 3) - 100) < 1e-6
    assert abs(valor_pgto(100, 4) - 110) < 1e-6
    assert valor_pgto(100, 5) is None  # teste opção inválida