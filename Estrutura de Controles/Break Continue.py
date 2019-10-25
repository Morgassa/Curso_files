from random import randint

def sortear_dado():
    return randint(1, 6)


def sortear_numero():
    dado = sortear_dado()
    for i in range(1,7):
        if i%2 == 1: # verificar se é ipar!
            continue
        elif i == dado:
            print('É o', dado, "Acertou Miseravel")
            break
    else:
        print('Vc é burro!')


sortear_numero()
sortear_dado()