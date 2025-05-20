def caesar_cipher(texto, desvio):
    texto_modificado = ""

    for cesar in texto:
        if cesar.isalpha():
            transforma_numero = ord(cesar) + desvio
            transforma_letra = chr(transforma_numero)
            texto_modificado += transforma_letra
        else:
            texto_modificado += cesar
            
    return(texto_modificado) 


def test():
    assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"
    assert caesar_cipher("Khoor, Zruog!", -3) == "Hello, World!"

    assert caesar_cipher("Matheus Jardim", 3) == "Pdwkhxv Mduglp"
    assert caesar_cipher("Pdwkhxv Mduglp", -3) == "Matheus Jardim"

    assert caesar_cipher(caesar_cipher("Atitus", 3), -3) == "Atitus"
    

