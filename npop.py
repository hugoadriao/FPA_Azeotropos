# faz a leitura da populacao e organiza como dicionario
def Npop(nome):
    with open(f'populacao/{nome}.txt', 'r') as f:
        items = [i.replace('\n', '') for i in f.readlines()]
        tupla = [tuple(map(float, i.split(','))) for i in items]
    dicio = {}
    n = 0
    for i in tupla:
        x, y, z = i
        dicio[n] = {'temp': x, 'frac_1': y, 'frac_2': z}
        n += 1
    return dicio