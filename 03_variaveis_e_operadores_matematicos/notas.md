def volume_do_cone (raio, altura):
    PI = 3.1
    return (PI*(raio**2)*altura)/(3)

def test():
    assert volume_do_cone( 5, 12) == 310

print(volume_do_cone(5, 12))

