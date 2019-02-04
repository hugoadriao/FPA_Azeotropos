from fpa import Fpa
from npop import Npop
from gera_pop import Popula_azeo
from gera_teste import Gera_mistura

op = input('gerar nova populacao?\nSIM = s\nNAO = n\n')
v_esp = 0
if(op == 's'):
    nome = input('nome do arquivo\n')
    Gera_mistura(nome)
    temp_min = 283
    temp_max = 473
    frac_min = 0
    frac_max = 1
    n = 20
    Popula_azeo(temp_min, temp_max, frac_min, frac_max, n, nome)
    dic = Npop(nome)
    saida = input('nome do arquivo de resultados\n')
    result = Fpa(0, dic, v_esp, saida)
    count = 1
    while result != True:
        result = Fpa(count, result, v_esp, saida)
        count += 1
else:
    nome = input('nome do arquivo\n')
    Gera_mistura(nome)
    dic = Npop(nome)
    saida = input('nome do arquivo de resultados\n')
    result = Fpa(0, dic, v_esp, saida)
    count = 1
    while result != True:
        result = Fpa(count, result, v_esp, saida)
        count += 1