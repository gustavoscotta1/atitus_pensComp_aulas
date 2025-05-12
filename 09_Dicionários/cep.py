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


def consuta_ceps_conhecidos(ceps_conhecidos, cep):
    for uf in ceps_conhecidos.keys():
        for localidade in ceps_conhecidos[uf].keys():
            if cep in ceps_conhecidos[uf][localidade]:
                return True
    return False


def main():
    contador_consultas = 0
    enderecos = {}

    while True:
        print("Você consultou um total de:", contador_consultas, "vezes")
        print("Dados em memória: ", enderecos)
        print()

        cep = input("Digite o seu cep:")
        if not is_cep_valid(cep):
            print("CEP inválido")
            continue

        if consuta_ceps_conhecidos(enderecos, cep):
            print("Já conhecemos este cep")
            continue

        contador_consultas += 1
        response = get_cep_data_from_api(cep)

        uf = response["uf"]
        localidade = response["localidade"]

        if uf in enderecos:
            if localidade in enderecos[uf]:
                enderecos[uf][localidade].append(cep)
            else:
                enderecos[uf][localidade] = [cep, ]
        else:
            enderecos[uf] = {localidade: [cep, ]}


main()


def validador_cep(cep):
    if len(cep) == 9:
       cep = cep.replace('-', '')
    if len(cep) != 8
       return False
    try:
       int(cep)
       return True
    except:
        return False


def add_endereco(cache, endereco):
    pass


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
}
resposta_01 = {"RS": {"Porto Alegre": ["91110-000"]}}
assert add_endereco({}, endereco_01) == resposta_01
assert add_endereco(resposta_01, endereco_01) == resposta_01
assert add_endereco(resposta_01, endereco_02) == {
    "RS": {"Porto Alegre": ["91110-000", "90240-111"]}
}
