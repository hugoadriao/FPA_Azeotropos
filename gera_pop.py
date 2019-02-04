import random


def Popula_azeo(temp_min, temp_max, frac_min, frac_max, n, nome):
    # lista de temperaturas
    temp = []
    # lista com parte das fracoes molares
    frac_1 = []  # fracao 1
    frac_2 = []  # fracao 2
    for i in range(0, n, 1):
        temp.append(random.uniform(temp_min, temp_max))
        frac_1.append(random.uniform(frac_min, frac_max))
        frac_2.append(1 - frac_1[i])
    lista = list(zip(temp, frac_1, frac_2))
    # d_pop = []
    n = len(lista)
    # for i in range(0, n, 1):
    #     d_pop.append(lista[i])
    with open(f'populacao/{nome}.txt', 'a+') as f:
        line = f.readline()
        if line == '':
            with open(f'populacao/{nome}.txt', 'w+')as f:
                for i in lista:
                    xn, yn, zn = i
                    f.write((f'{xn},{yn},{zn}\n'))
        else:
            return 0