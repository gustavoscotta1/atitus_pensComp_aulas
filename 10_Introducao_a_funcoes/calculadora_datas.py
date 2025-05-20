"""
Meses sao representados como: 1=Jan, 2=Feb, 3=Mar..
"""

MESES_31_DIAS = [1, 3, 5, 7, 8, 10, 12]
MESES_30_DIAS = [4, 6, 9, 11]

def eh_bissexto(ano: int) -> bool:
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

def total_dias_no_mes(mes: int, ano: int) -> int:
    if mes in MESES_31_DIAS:
        return 31
    elif mes in MESES_30_DIAS:
        return 30
    else:
        # Fevereiro
        return 29 if eh_bissexto(ano) else 28

def formata_data(data: list) -> str:
    dia, mes, ano = data
    return f"{dia}/{mes}/{ano}"

def calcula_diferenca(data1: list, data2: list) -> int:
    def dias_desde_ano_zero(data: list) -> int:
        dia, mes, ano = data
        dias = 0
        for a in range(1, ano):
            dias += 366 if eh_bissexto(a) else 365
        for m in range(1, mes):
            dias += total_dias_no_mes(m, ano)
        dias += dia
        return dias

    return abs(dias_desde_ano_zero(data1) - dias_desde_ano_zero(data2))


def test():
    assert total_dias_no_mes(1, 2024) == 31
    assert total_dias_no_mes(2, 2024) == 29
    assert total_dias_no_mes(3, 2024) == 31
    assert total_dias_no_mes(11, 2024) == 30

    assert formata_data([1, 2, 2024]) == "1/2/2024"
    assert formata_data([1, 12, 2024]) == "1/12/2024"

    assert calcula_diferenca([2, 7, 2004], [27, 5, 2024]) == 7269
    assert calcula_diferenca([27, 5, 2024], [2, 7, 2089]) == 23779
    assert calcula_diferenca([2, 7, 2004], [2, 7, 2089]) == 31047
    assert calcula_diferenca([24, 7, 1991], [24, 10, 2024]) == 12146
    assert calcula_diferenca([24, 10, 2024], [24, 7, 2076]) == 18900
    assert calcula_diferenca([24, 7, 1991], [24, 7, 2076]) == 31046