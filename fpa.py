from azeo import Azeo
from poli_global import Poli_global3
from poli_local import Poli_local3
from levy import Levy
import random


count_func = 0


def Fpa(n, dic, v_esp, saida_nome):
    # variavel global responsavel por armazenar o total de vezes que a funca problema e utilizada no codigo
    global count_func
    # variavel temporaria para o armazenamento do numero de vezes que a funcao problema e utilizada no codigo
    temp_count_func = 0
    # variavel de tolerancia
    tol = pow(10, -8)
    # variavel utilizada para setar a probabilidade de polinizacao global
    prob = 0.8
    # variavel utilizada para armazenar os individous
    popula = dic
    # variavel utilizada para armazenar os novos individous
    print(dic)
    n_popula = {}
    # variavel utilizada para armazenar o melhor individou
    g = {}
    # variavel utilizada para armazenar as aptidoes do individuos
    aptd = []
    # limites
    temp_min = 283
    temp_max = 473
    frac_min = 0
    frac_max = 1
    # calculo de aptidao, os valores de cada individou e utilizado na funcao
    for i in popula.values():
        # print('indv', i)
        valor = Azeo(i)
        aptd.append(valor)
        temp_count_func += 1
    # atribui o primeiro elemento para futuro teste
    # print('ok')
    pivot = aptd[0]
    # atribui o primeiro individou apenas para ja possuir valor
    g = popula[0]
    # verifica qual individou tem a melhor aptidao
    for i in popula.keys():
        # checando populacao
        if pivot > aptd[i]:
            pivot = aptd[i]
            # armazena o individou com melhor aptidao
            g = popula[i]
    # teste de probabilidade de ocorrer polinizacao global
    # Polinizacao global
    # print('ok')
    if (random.uniform(0, 1) <= prob):
        l = Levy(n)
        for i in popula.keys():
            n_popula[i] = Poli_global3(popula[i], g, l)
    # Polinizacao local
    else:
        count = len(dic)-1
        a = random.randint(0, count)
        b = random.randint(0, count)
        while a == b:
            b = random.randint(0, count)
        b_a1 = popula[a]
        b_a2 = popula[b]
        for i in popula.keys():
            n_popula[i] = Poli_local3(popula[i], b_a1, b_a2)

    for i in n_popula.keys():
        if (n_popula[i]['frac_1'] < frac_min):
            n_popula[i]['frac_1'] = frac_min+(0.3*random.uniform(0, 1))
            n_popula[i]['frac_2'] = 1 - n_popula[i]['frac_1']

        if (n_popula[i]['frac_1'] > frac_max):
            n_popula[i]['frac_1'] = frac_max-(0.3*random.uniform(0, 1))
            n_popula[i]['frac_2'] = 1 - n_popula[i]['frac_1']

        if (n_popula[i]['temp'] < temp_min):
            n_popula[i]['temp'] = temp_min+(0.3*random.uniform(0, 1))

        if (n_popula[i]['temp'] > temp_max):
            n_popula[i]['temp'] = temp_max-(0.3*random.uniform(0, 1))

    # checa e organiza os novos valores
    # print('ok')
    for i in popula.keys():
        # print('indv', popula[i])
        old_indv = Azeo(popula[i])
        temp_count_func += 1
        # print('indv', n_popula[i])
        new_indv = Azeo(n_popula[i])
        temp_count_func += 1
        if new_indv < old_indv:
            popula[i] = n_popula[i]
    n_aptd = []
    # print('ok')
    # procura pelo novo melhor individuo
    for i in popula.values():
        # print('indv', i)
        n_aptd.append(Azeo(i))
        temp_count_func += 1
    pivot = n_aptd[0]
    g = popula[0]
    for i in popula.keys():
        # checando populacao
        if pivot > n_aptd[i]:
            pivot = n_aptd[i]
            # armazena o individou com melhor aptidao
            g = popula[i]
    temp_count_func += 1
    count_func += temp_count_func
    if abs(v_esp - pivot) <= tol:
        # print('resultado')
        with open(f'result/{saida_nome}.txt', 'a') as f:
            # f.write(f'solucao: {g}\n')
            # f.write(f'numero de iteracoes: {n}\n')
            # f.write(f'aptidao: {pivot}\n')
            # f.write(
            #     f'numero de vezes que a funcao foi utilizada: {count_func}')
            # f.write('\n------------------------------------------------\n')
            f.write(f'\n{n};{count_func};{g};{pivot}')
            count_func = 0
        return True
    else:
        return popula