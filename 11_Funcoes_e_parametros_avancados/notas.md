def verifica_repetido(texto: str) -> bool: 
    lista_nova = []
    lista_de_palavras = texto.split(" ")
    for palavra in lista_de_palavras:
        if (palavra in lista_nova):
            return True
        lista_nova.append(palavra)
    return False


    