import math
def baskhara(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None
    elif discriminante == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return [x1, x2]

def test():
    assert baskhara(1, -3, 2) == [2, 1]
    assert baskhara(2, 3, -2) == [0.5, -2]
    assert baskhara(1, -5, 6) == [3, 2]
    assert baskhara(1, -7, 10) == [5, 2]

    assert baskhara(1, 2, 3) is None
    assert baskhara(1, 0, 0) == 0
