def baskhara(a, b, c):
discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None
    elif discriminante == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + (discriminante)** 0.5) / (2 * a)
        x2 = (-b - (discriminante)** 0.5) / (2 * a)
        return [x1, x2]


assert baskhara(1, -3, 2) == [2, 1]
assert baskhara(2, 3, -2) == [-2, 0.5]
assert baskhara(1, -5, 6) == [2, 3]
assert baskhara(1, -7, 10) == [2, 5]

assert baskhara(1, 2, 3) is None
assert baskhara(1, 0, 0) == 0
