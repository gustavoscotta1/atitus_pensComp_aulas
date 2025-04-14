def descobre_senha():
    SENHA = 10  
    tentativas = 0 

    while True:
        numero = int(input('Digite a senha: '))  
        tentativas += 1  
        
        if numero == SENHA:  
            print(f"Senha correta! Você acertou em {tentativas} tentativas.")
            break  
        else:
            print("Senha incorreta. Tente novamente.")
    