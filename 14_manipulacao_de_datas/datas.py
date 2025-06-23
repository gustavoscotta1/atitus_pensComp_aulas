from datetime import date, datetime
import calendar





def str_to_date(date_str):
    try:
        d = datetime.strptime(date_str, "%d-%m-%Y").date()
        return d
    except ValueError:
        return None

def test_str_to_date():
    assert str_to_date('10-01-2025') == date(day=10, month=1, year=2025)
    assert str_to_date('10-99-2025') is None



def nome_dia_semana(data):
    nomes = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    return nomes[data.weekday()]

def test_nome_dia_semana():
    assert nome_dia_semana(date(year=2025, month=1, day=1)) == 'quarta-feira'
    assert nome_dia_semana(date(year=2025, month=1, day=2)) == 'quinta-feira'



def dias_para_finde(data):
    dias_ate_sabado = 5 - data.weekday()
    return dias_ate_sabado if dias_ate_sabado >= 0 else 0

def test_dias_para_finde():
    assert dias_para_finde(date(year=2025, month=1, day=1)) == 3
    assert dias_para_finde(date(year=2025, month=1, day=2)) == 2



def delta_dias(data_a, data_b):
    return (data_b - data_a).days if (data_b - data_a).days != 1 else 0

def test_delta_dias():
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2026, month=1, day=2)) == 365
    assert delta_dias(date(year=2026, month=1, day=1), date(year=2025, month=1, day=2)) == -365
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2025, month=1, day=2)) == 0



def proximo_mes(data_a):
    ano = data_a.year
    mes = data_a.month + 1
    if mes > 12:
        mes = 1
        ano += 1
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    dia = min(data_a.day, ultimo_dia)
    return date(ano, mes, dia)

def test_proximo_mes():
    assert proximo_mes(date(year=2025, month=1, day=1)) == date(year=2025, month=2, day=1)
    assert proximo_mes(date(year=2025, month=1, day=29)) == date(year=2025, month=2, day=28)
    assert proximo_mes(date(year=2024, month=1, day=29)) == date(year=2024, month=2, day=29)
    assert proximo_mes(date(year=2025, month=1, day=30)) == date(year=2025, month=2, day=28)

def data_futuro(data: date) -> int:
    hoje = date.today()
    if data > hoje:
        return 1
    elif data < hoje:
        return -1
    else:
        return 0

def test_data_futuro():
    assert data_futuro(date(day=1, month=1, year=2099)) == 1
    assert data_futuro(date(day=1, month=1, year=1999)) == -1
    assert data_futuro(date.today()) == 0

