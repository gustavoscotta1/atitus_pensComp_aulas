def letra_em_texto(texto, letra):
    for caractere in texto:
        if caractere == letra:
            return True
    return False


def conta_letra_em_texto(texto, letra):
    contador = 0
    for caractere in texto:
        if caractere == letra:
            contador += 1
    return contador


def texto_sem_letra(texto, letra):
    novo_texto = ""
    for caractere in texto:
        if caractere != letra:
            novo_texto += caractere
    return novo_texto


def texto_com_letra_upper(texto, letra):
    novo_texto = ""
    for caractere in texto:
        if caractere == letra:
            novo_texto += caractere.upper()
        else:
            novo_texto += caractere
    return novo_texto

# texto = input("Digite um texto: ")
# letra = input("Digite a letra que deseja analisar: ")

print("\nEscolha a opção desejada:")
print("1 - Verificar se a letra está no texto")
print("2 - Contar quantas vezes a letra aparece no texto")
print("3 - Mostrar o texto sem a letra")
print("4 - Mostrar o texto com a letra em maiúsculo")

opcao = input("Digite o número da opção: ")

if opcao == "1":
    if letra_em_texto(texto, letra):
        print(f"A letra '{letra}' está no texto.")
    else:
        print(f"A letra '{letra}' NÃO está no texto.")
elif opcao == "2":
    contagem = conta_letra_em_texto(texto, letra)
    print(f"A letra '{letra}' aparece {contagem} vez(es) no texto.")
elif opcao == "3":
    novo = texto_sem_letra(texto, letra)
    print(f"Texto sem a letra '{letra}':\n{novo}")
elif opcao == "4":
    novo = texto_com_letra_upper(texto, letra)
    print(f"Texto com a letra '{letra}' em maiúsculo:\n{novo}")
else:
    print("Opção inválida.")

def test(): 
    assert letra_em_texto("Pensamento Computacional", "a")
    assert letra_em_texto("Pensamento Computacional", " ")
    assert not letra_em_texto("Pensamento Computacional", "A")
    assert not letra_em_texto("Pensamento Computacional", "c")

    assert conta_letra_em_texto("Pensamento Computacional", "a") == 3
    assert conta_letra_em_texto("Pensamento Computacional", "A") == 0
    assert conta_letra_em_texto("Pensamento Computacional", "e") == 2

    assert texto_sem_letra("Pensamento Computacional", "a") == "Pensmento Computcionl"
    assert texto_sem_letra("Pensamento Computacional", "z") == "Pensamento Computacional"
    assert texto_sem_letra("Pensamento Computacional", " ") == "PensamentoComputacional"

    assert (
    texto_com_letra_upper("Pensamento Computacional", "a") == "PensAmento ComputAcionAl"
    )
    assert (
    texto_com_letra_upper("Pensamento Computacional", "z") == "Pensamento Computacional"
    )
    assert (
    texto_com_letra_upper("Pensamento Computacional", " ") == "Pensamento Computacional"
    )
