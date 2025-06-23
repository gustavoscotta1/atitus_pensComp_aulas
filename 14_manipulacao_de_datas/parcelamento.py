from datetime import date
import calendar

def proximo_mes(data_a):
    ano = data_a.year
    mes = data_a.month + 1
    if mes > 12:
        mes = 1
        ano += 1
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    dia = min(data_a.day, ultimo_dia)
    return date(ano, mes, dia)

def parcelamento(valor, parcelas, dt_venda):
    base = valor // parcelas
    resto = valor % parcelas
    resultado = []
    data_parcela = dt_venda

    for i in range(parcelas):
        valor_parcela = base + (1 if i >= parcelas - resto else 0)
        resultado.append([valor_parcela, data_parcela])
        data_parcela = proximo_mes(data_parcela)

    return resultado

def test_parcelamento():
    data_venda = date(2025, 1, 31)

    assert parcelamento(100, 1, data_venda) == [[100, data_venda]]
    assert parcelamento(100, 2, data_venda) == [
        [50, data_venda],
        [50, date(2025, 2, 28)]
    ]
    assert parcelamento(100, 3, data_venda) == [
        [33, data_venda],
        [33, date(2025, 2, 28)],
        [34, date(2025, 3, 31)]
    ]
    assert parcelamento(100, 4, data_venda) == [
        [25, data_venda],
        [25, date(2025, 2, 28)],
        [25, date(2025, 3, 31)],
        [25, date(2025, 4, 30)]
    ]
    assert parcelamento(100, 6, data_venda) == [
        [16, data_venda],
        [16, date(2025, 2, 28)],
        [17, date(2025, 3, 31)],
        [17, date(2025, 4, 30)],
        [17, date(2025, 5, 31)],
        [17, date(2025, 6, 30)]
    ]
