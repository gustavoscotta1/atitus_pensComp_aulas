IDADE_PARA_MAIORIDADE = 18


def verifica_maioridade(idade: int) -> bool:
    return isinstance(idade, int) and idade >= IDADE_PARA_MAIORIDADE


def verifica_email(email: str) -> bool:
    if not isinstance(email, str) or email.count('@') != 1:
        return False
    usuario, dominio = email.split('@')
    if not usuario or not dominio:
        return False
    partes_dominio = dominio.split('.')
    if len(partes_dominio) != 2:
        return False
    dominio_nome, dominio_ext = partes_dominio
    if not dominio_nome.isalnum() or not dominio_ext.isalpha():
        return False
    return True


def solicita_nome() -> str | None:
    nome = input("Digite seu nome: ").strip()
    return nome if nome else None


def test_verifica_maioridade():
    assert not verifica_maioridade(-1)
    assert not verifica_maioridade(0)
    assert not verifica_maioridade(1)
    assert not verifica_maioridade(17)
    assert verifica_maioridade(18)
    assert verifica_maioridade(20)
    assert verifica_maioridade(100)

def test_verifica_email(): 
    assert not verifica_email('')
    assert not verifica_email('@')
    assert not verifica_email('@@')
    assert not verifica_email('abc@@abc.com')
    assert not verifica_email('abc@abc.edu')
    assert not verifica_email('a_b_c@a_b_c.com.com')
    assert not verifica_email('a_b_c@a_b_c.com.com.com')
    
    assert verifica_email('ABC@a_b_c.com')
    assert verifica_email('ABC@ABC.com')
    assert verifica_email('AbC@1BC.com')
    assert verifica_email('abc@abc.com')
    assert verifica_email('a23@123.com')
    assert verifica_email('a_b_c@a_b_c.com')
