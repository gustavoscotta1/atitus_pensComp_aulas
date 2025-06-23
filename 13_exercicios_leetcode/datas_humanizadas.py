MINUTO = 60
HORA = 60 * MINUTO

def data_humanizada(duracao: int) -> str:
    horas = duracao // HORA
    duracao %= HORA
    minutos = duracao // MINUTO
    segundos = duracao % MINUTO

    partes = []
    if horas > 0:
        if horas == 1:
            partes.append(f"{horas} hora")
        else:
            partes.append(f"{horas} horas")
    if minutos > 0:
        if minutos == 1:
            partes.append(f"{minutos} minuto")
        else:
            partes.append(f"{minutos} minutos")
    if segundos > 0 or (horas == 0 and minutos == 0):
        if segundos == 1:
            partes.append(f"{segundos} segundo")
        else:
            partes.append(f"{segundos} segundos")

    return ' '.join(partes)

def test_data_humanizada():
    assert data_humanizada(10) == "10 segundos"
    assert data_humanizada(1 * MINUTO) == "1 minuto"
    assert data_humanizada(2 * MINUTO) == "2 minutos"
    assert data_humanizada(2 * MINUTO + 20) == "2 minutos 20 segundos"
    assert data_humanizada(2 * HORA + 3 * MINUTO + 20) == "2 horas 3 minutos 20 segundos"

