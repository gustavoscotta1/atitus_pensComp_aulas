def desenha_losango(altura):
    if altura % 2 == 0:
        print("A altura deve ser um número ímpar.")
        return
meio = altura // 2
    for i in range(meio + 1):
        espacos = ' ' * (meio - i)
        estrelas = '*' * (2 * i + 1)
        print(espacos + estrelas)
    for i in range(meio - 1, -1, -1):
        espacos = ' ' * (meio - i)
        estrelas = '*' * (2 * i + 1)
        print(espacos + estrelas)


# altura = int(input("Digite um valor ímpar para a altura do losango: "))
desenha_losango(7)
