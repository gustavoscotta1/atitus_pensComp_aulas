def real_para_dolar(valor, tx_conversao):
    if tx_conversao == 0:
        return None  
    return valor / tx_conversao

# valor = float(input("Digite o valor em reais (R$): "))
# taxa = float(input("Digite a taxa de conversão (ex: 5.20): "))

resultado = real_para_dolar(valor, taxa)

if resultado is not None:
    print(f"O valor em dólares é: ${resultado}")
else:
    print("A taxa de conversão não pode ser zero.")

def test():
    assert real_para_dolar(500, 5.20) == 96.23
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 83.33333333333333
