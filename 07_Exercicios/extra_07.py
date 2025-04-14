def fahrenheit_para_celsius(valor):
    return (valor - 32) * 5 / 9


def celsius_para_fahrenheit(valor):
    return valor * 9 / 5 + 32


def test(): 
    assert fahrenheit_para_celsius(104) == 40
    assert fahrenheit_para_celsius(-13) == -25

    assert celsius_para_fahrenheit(40) == 104
    assert celsius_para_fahrenheit(-25) == -13

    assert celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30
