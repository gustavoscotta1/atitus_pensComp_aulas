import os

def criar_pasta(pasta):
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        return f"A pasta '{pasta}' foi criada com sucesso."
    else:
        return f"A pasta '{pasta}' já existe."

def test_criar_pasta():
    pasta = "minha_pasta"

    resultado = criar_pasta(pasta)
    assert resultado in [
        f"A pasta '{pasta}' foi criada com sucesso.",
        f"A pasta '{pasta}' já existe."
    ]
