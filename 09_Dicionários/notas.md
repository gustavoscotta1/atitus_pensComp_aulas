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