def dec_para_bin(valor): 
    if valor < 0:
        return ''
    if valor == 0:
        return '0'
    reslutado = ''
    while valor > 0:
        resultado = str(valor % 2) + resultado
        valor = valor // 2
    return resultado 
    
        
def bin_para_dec(valor): 
    res = 0
    potencia = len(val) - 1
    for char in val:
        res = res + int(char) * (2 ** potencia)
        potencia -= 1
    return res





def test():
    assert dec_para_bin(10) == '1010'
    assert bin_para_dec('1010') == 10 




    import http.client
import json

def obtem_dados_endereco(cep):
    url = f"/ws/{cep}/json/"
    conn = http.client.HTTPSConnection("viacep.com.br")
    conn.request("GET", url)
    response = json.loads(conn.getresponse().read().decode())
    conn.close()

    # Verifica se o CEP é inválido
    if "erro" in response:
        return None

    return response

def validador_cep(cep):
    cep = cep.strip().replace('-', '')  
    if len(cep) != 8:
        return False
    try:
        int(cep)
        return True
    except ValueError:
        return False

cache_cep = {}

consultas_externas = 0
cidades_por_estado = {}

while True:
    cep = input("Digite um CEP (ou '0' para encerrar): ").strip()

    if cep == '0':
        break

    if not validador_cep(cep):
        print("CEP inválido. Tente novamente.\n")
        continue

    cep = cep.replace('-', '')  # Normaliza o formato

    if cep in cache_cep:
        print("CEP encontrado no cache.")
        dados = cache_cep[cep]
    else:
        print(" Consultando serviço externo...")
        dados = obtem_dados_endereco(cep)

        if dados is None:
            print("CEP não encontrado na base do ViaCEP.\n")
            continue

        cache_cep[cep] = dados
        consultas_externas += 1

    estado = dados['uf']
    cidade = dados['localidade']

    if estado not in cidades_por_estado:
        cidades_por_estado[estado] = set()
    cidades_por_estado[estado].add(cidade)

    print(f"Resultado: {cidade}, {estado}\n")


print("\n Resumo das cidades consultadas por estado:")
for estado, cidades in sorted(cidades_por_estado.items()):
    print(f"{estado}: {len(cidades)} cidade(s)")

print(f"\n Total de consultas feitas ao serviço externo: {consultas_externas}")