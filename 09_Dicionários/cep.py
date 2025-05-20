import http.client
import json

LEN_CEP = 8

def get_cep_data_from_api(val):
    url = f"/ws/{val}/json/"
    conn = http.client.HTTPSConnection("viacep.com.br")
    conn.request("GET", url)
    response = json.loads(conn.getresponse().read().decode())
    conn.close()
    return response

def is_cep_valid(val):
    if len(val) != LEN_CEP:
        return False
    for char in val:
        if not char.isdigit():
            return False
    return True

def consulta_ceps_conhecidos(ceps_conhecidos, cep):
    for uf in ceps_conhecidos.keys():
        for localidade in ceps_conhecidos[uf].keys():
            if cep in ceps_conhecidos[uf][localidade]:
                return True
    return False

def validador_cep(cep):
    if len(cep) == 9:
        cep = cep.replace('-', '')
    if len(cep) != 8:
        return False
    try:
        int(cep)
        return True
    except:
        return False

def add_endereco(cache, endereco):
    cep = endereco.get("cep", "").replace('-', '')
    uf = endereco.get("uf")
    localidade = endereco.get("localidade")

    if not uf or not localidade:
        return cache

    if uf not in cache:
        cache[uf] = {}

    if localidade not in cache[uf]:
        cache[uf][localidade] = []

    if cep not in cache[uf][localidade]:
        cache[uf][localidade].append(cep)

    return cache


def test():
    assert validador_cep("99110000")
    assert validador_cep("99110-000")
    assert not validador_cep("99110 000")
    assert not validador_cep("9911-0000")
    assert not validador_cep("99110000 ")
    assert not validador_cep(" 99110000")
    assert not validador_cep("9911000")

endereco_01 = {
    "cep": "91110-000",
    "logradouro": "Avenida Assis Brasil",
    "localidade": "Porto Alegre",
    "uf": "RS",
}
endereco_02 = {
    "cep": "90240-111",
    "logradouro": "Rua Frederico Mentz",
    "localidade": "Porto Alegre",
    "uf": "RS",
}
resposta_01 = {"RS": {"Porto Alegre": ["91110000"]}}
    assert add_endereco({}, endereco_01) == resposta_01
    assert add_endereco(resposta_01, endereco_01) == resposta_01
    assert add_endereco(resposta_01, endereco_02) == {
    "RS": {"Porto Alegre": ["91110000", "90240111"]}
}
