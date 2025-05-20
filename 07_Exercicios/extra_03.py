def real_para_dolar(valor, taxa):
    if taxa == 0:
        return None  
    return valor / taxa


def test():
    assert abs(real_para_dolar(500, 5.20) - 96.15384615384616) < 1e-9
    assert real_para_dolar(500, 1) == 500
    assert abs(real_para_dolar(500, 6) - 83.33333333333333) < 1e-9
    assert real_para_dolar(500, 0) is None