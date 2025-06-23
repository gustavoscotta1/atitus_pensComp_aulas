def imprimir_calendario_mes(dia_inicial: int, total_dias: int):
    cabecalho = "Do.Se.Te.Qu.Qu.Se.Sá"
    calendario = [cabecalho]

    linha = "." * (dia_inicial * 3)
    dia = 1

    while dia <= total_dias:
        while len(linha) < 20 and dia <= total_dias:
            if len(linha) > 0 and linha[-1] != '.':
                linha += '.'
            if dia < 10:
                linha += f"{dia}."
            else:
                linha += f"{dia}."
            dia += 1
        calendario.append(linha.rstrip('.'))
        linha = ""

    return calendario

def test_imprimir_calendario_mes():
    assert imprimir_calendario_mes(0, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        ".1..2..3..4..5..6..7",
        ".8..9.10.11.12.13.14",
        "15.16.17.18.19.20.21",
        "22.23.24.25.26.27.28",
        "29.30.31",
    ]

    assert imprimir_calendario_mes(1, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        "....1..2..3..4..5..6",
        ".7..8..9.10.11.12.13",
        "14.15.16.17.18.19.20",
        "21.22.23.24.25.26.27",
        "28.29.30.31",
    ]

    assert imprimir_calendario_mes(2, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        ".......1..2..3..4..5",
        ".6..7..8..9.10.11.12",
        "13.14.15.16.17.18.19",
        "20.21.22.23.24.25.26",
        "27.28.29.30.31",
    ]
