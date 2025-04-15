# Gustavo Scotta e Caue Castro 

ano_nascimento = int(input("Em que ano você nasceu?"))
idade_aposentar = int(input("Com quantos anos você quer se aposentar?"))
expectativa_vida = int(input("Qual sua expectativa de vida?"))
patrimonio = int(input("Qual o seu patrimônio atual?"))
taxa_crescimento = int(input("Qual a taxa anual de crescimento?"))
aporte_mensal = int(input("Quanto você vai guardar por mês?"))
custo_aposentadoria = int(input("Quanto você quer gastar por mês?"))

ANO_ATUAL = 2025
Idade = ANO_ATUAL - ano_nascimento
Aposentadoria = ano_nascimento + idade_aposentar
Ano_morte = ano_nascimento + expectativa_vida
Anos_que_faltam = Aposentadoria - ANO_ATUAL
Taxa_anual_para_mensal = (1 + (taxa_crescimento / 100)) ** (1 / 12) - 1
Taxa_mensal = 1 + Taxa_anual_para_mensal
Meses_aposentar = 12 * Anos_que_faltam
Meses_aposentado = (Ano_morte - Aposentadoria) * 12


print (Taxa_anual_para_mensal)
for i in range(Meses_aposentar+12):
    patrimonio = (patrimonio * Taxa_mensal) + aporte_mensal
    print("O seu valor de patrimônio guardado foi de:", patrimonio)

for i in range(Meses_aposentado+1):
    patrimonio = (patrimonio * Taxa_mensal) - custo_aposentadoria
    print("A herança deixada é de:", patrimonio)