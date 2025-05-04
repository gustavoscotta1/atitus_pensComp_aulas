import random  # Sorteia palavras aleatoriamente

# Listas de palavras, separadas por comprimento (5, 6 ou 7 letras)
PALAVRAS = {
    5: ['limao', 'amora', 'banco', 'carta', 'dente', 'folha', 'grade', 'honra', 'carne', 'feira', 'limpo', 'manga', 'noite', 'livro', 'pedra', 'tinta', 'roupa', 'sabor', 'tampa', 'praia', 'velho', 'vinho', 'sonho', 'lenda', 'manto'],
    6: ['banana', 'jardim', 'retina', 'correr', 'lanche', 'seguro', 'motivo', 'direto', 'janela', 'chance', 'origem', 'batata', 'viagem', 'alface', 'contra', 'truque', 'alface', 'temido', 'formal', 'objeto', 'acento', 'isento', 'prazer', 'sempre', 'rotina'],
    7: ['marisco', 'pantano', 'empatia', 'cultura', 'virtude', 'desenho', 'pintura', 'mercado', 'sucesso', 'alegria', 'orgulho', 'saudade', 'coragem', 'modesto', 'parcial', 'vigente', 'piedade', 'sentido', 'bizarro', 'intenso', 'ousadia', 'desafio', 'palavra', 'intuito', 'cuidado']
}

# Função para exibir as regras do jogo
def exibir_regras():
    print("==============================================")
    print("            Bem-vindo ao TERM.OOO!          ")
    print("==============================================")
    print("Regras do jogo:")
    print("1. Escolha a dificuldade: palavras de 5, 6 ou 7 letras.")
    print("2. Você terá um número de tentativas igual ao comprimento da palavra.")
    print("3. Após cada tentativa, receberá dicas sobre suas letras:")
    print("   - [✔] Letra correta e na posição certa.")
    print("   - [?] Letra correta, mas na posição errada.")
    print("   - [ ] Letra errada.")
    print("4. As palavras não possuem acentos e a avaliação ignora maiúsculas/minúsculas.\n")

# Função para obter a dificuldade escolhida pelo jogador
def obter_dificuldade():
    while True:
        dificuldade = input("Escolha a dificuldade (5, 6 ou 7): ").strip()
        # Verifica se o valor inserido é válido
        if dificuldade in ['5', '6', '7']:
            return int(dificuldade)  # Retorna o número como inteiro
        else:
            print("Entrada inválida. Por favor, digite 5, 6 ou 7.")

# Função para sortear uma palavra aleatória com base na dificuldade escolhida
def sortear_palavra(tamanho):
    return random.choice(PALAVRAS[tamanho]).lower()  # Escolhe uma palavra da lista e converte para minúsculas

# Função que pede ao jogador que insira um palpite de palavra
def obter_palpite(tamanho):
    while True:
        palpite = input(f"Digite sua tentativa de {tamanho} letras: ").strip().lower()
        # Valida o palpite: tamanho correto e apenas letras
        if len(palpite) != tamanho:
            print(f"Por favor, digite exatamente {tamanho} letras.")
        elif not palpite.isalpha():
            print("Entrada inválida. Use apenas letras.")
        else:
            return palpite  # Retorna o palpite válido

# Função que avalia o palpite comparando com a palavra secreta
def avaliar_palpite(palpite, palavra_secreta):
    dicas = ['' for _ in range(len(palpite))]  # Lista que armazenará as dicas (um item para cada letra)
    letras_restantes = list(palavra_secreta)  # Cópia da palavra secreta para controle de letras já usadas

    # Primeira verificação: letras na posição correta
    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:  # Letra correta na posição correta
            dicas[i] = f"[✔] {palpite[i].upper()}"  # Marca como acerto com símbolo ✔
            letras_restantes[i] = None  # Remove essa letra da lista de comparação
        else:
            dicas[i] = None  # Marca posição para segunda verificação

    # Segunda verificação: letras corretas, mas em posições erradas
    for i in range(len(palpite)):
        if dicas[i] is None:  # Apenas se não já foi marcada como correta
            if palpite[i] in letras_restantes:  # Letra existe em outra posição
                dicas[i] = f"[?] {palpite[i].upper()}"  # Marca como parcialmente correta
                letras_restantes[letras_restantes.index(palpite[i])] = None  # Remove essa letra para não ser reutilizada
            else:
                dicas[i] = f"[ ] {palpite[i].upper()}"  # Letra não existe na palavra

    return dicas  # Retorna a lista de dicas

# Função que executa uma rodada do jogo (do início ao fim)
def jogar_rodada():
    exibir_regras()  # Mostra as instruções
    tamanho = obter_dificuldade()  # Obtém a dificuldade escolhida
    palavra_secreta = sortear_palavra(tamanho)  # Sorteia a palavra secreta com o número de letras escolhido
    max_tentativas = tamanho  # Define o número máximo de tentativas igual ao tamanho da palavra
    tentativas = 0  # Inicializa o contador de tentativas

    # Loop das tentativas do jogador
    while tentativas < max_tentativas:
        palpite = obter_palpite(tamanho)  # Solicita um novo palpite ao jogador
        tentativas += 1  # Incrementa o número de tentativas feitas

        if palpite == palavra_secreta:  # Se acertou a palavra inteira
            print(f"\nParabéns! Você acertou a palavra '{palavra_secreta.upper()}' em {tentativas} tentativas!")
            return  # Encerra a rodada

        dicas = avaliar_palpite(palpite, palavra_secreta)  # Avalia o palpite e gera dicas
        print("Dicas:", '  '.join(dicas))  # Exibe as dicas ao jogador

    # Se esgotou as tentativas sem acertar
    print(f"\nFim de jogo! A palavra correta era: {palavra_secreta.upper()}")

# Função principal que controla o fluxo contínuo do jogo (permite jogar várias vezes)
def jogar():
    while True:
        jogar_rodada()  # Executa uma rodada completa
        novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if novamente != 's':
            print("Obrigado por jogar! Até a próxima.")
            break  # Encerra o jogo se o jogador não quiser continuar

# Verifica se o arquivo está sendo executado diretamente (e não importado)
if __name__ == "__main__":
    jogar()  # Inicia o jogo