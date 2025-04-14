import os
import time

def anima_letra_A(largura=40, altura=10, duracao=100):
    x, y = 0, 0  
    dx, dy = 1, 1  
    encostou = 0

    for _ in range(duracao):
        os.system('cls' if os.name == 'nt' else 'clear')

        for linha in range(altura):
            if linha == y:
                print(' ' * x + 'A')  
            else:
                print()  

        time.sleep(0.05)

        x += dx
        y += dy

        if x <= 0 or x >= largura - 1:
            dx *= -1
            encostou += 1

        if y <= 0 or y >= altura - 1:
            dy *= -1
            encostou += 1

    print(f'\nA letra "A" encostou nas paredes {encostou} vezes.')

    anima_letra_A()