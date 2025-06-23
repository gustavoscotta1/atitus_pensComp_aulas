import os
import unicodedata


def limpa_nome_pasta(nome: str) -> str:
    nome = nome.lower().replace(' ', '_')
    nome = unicodedata.normalize('NFD', nome).encode('ascii', 'ignore').decode('utf-8')
    return nome


def cria_pasta_curso(nome_curso: str) -> None:
    nome_pasta = limpa_nome_pasta(nome_curso)
    if not os.path.exists(nome_pasta):
        os.mkdir(nome_pasta)


def cria_alunos(alunos: list, nome_curso: str) -> None:
    nome_pasta = limpa_nome_pasta(nome_curso)
    cria_pasta_curso(nome_curso)
    for aluno in alunos:
        caminho = os.path.join(nome_pasta, f"{aluno}.txt")
        with open(caminho, 'w') as f:
            f.write(f"Aluno: {aluno}\nCurso: {nome_curso}")


def converte_alunos_em_lista(alunos_com_virgula: str) -> list:
    return [aluno.strip() for aluno in alunos_com_virgula.split(',') if aluno.strip()]


def test_limpa_nome_pasta():
    assert limpa_nome_pasta('Ciência da Computação') == 'ciencia_da_computacao'
    assert limpa_nome_pasta('Administração') == 'administracao'


def test_converte_alunos_em_lista():
    assert converte_alunos_em_lista('João, Maria, Ana') == ['João', 'Maria', 'Ana']
    assert converte_alunos_em_lista('  Pedro ,  Carla ') == ['Pedro', 'Carla']
    assert converte_alunos_em_lista('') == []
