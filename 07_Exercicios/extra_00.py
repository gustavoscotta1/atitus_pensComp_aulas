ANO_ATUAL = 2025


def saudacao(nome, sobrenome, ano_nascimento):

nome = input('Qual o seu nome?')
sobrenome = input('Qual o seu sobrenome?')
ano_nascimento = int(input('Que ano você nasceu?'))
idade = ANO_ATUAL - ano_nascimento
print(f'olá, "{nome} {sobrenome}". Bom dia! você possui {idade}!')


def test():
    assert (
    saudacao("Matheus", "Jardim", 1991)
    == "Olá, Matheus Jardim. Bom dia! Você possui 33 anos!"
    )
    assert (
    saudacao("Thais", "Silva", 1990)
    == "Olá, Thais Silva. Bom dia! Você possui 34 anos!"
    )
    assert saudacao("Matheus", "Jardim", 0) is None
    assert saudacao("Matheus", "Jardim", 2050) is None
