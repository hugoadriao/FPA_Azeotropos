from math import log
from elementos import Elemento
from psat import Psat
from misturas import Mistura
from nrtl import Nrtl
from gera_teste import Catch_nome


def Azeo(indv):
    # nome1 = indv['nome1']
    # nome2 = indv['nome2']
    # nome1 = 'cloroform'
    # nome1 = 'acetone'
    # nome1 = 'benzene'
    # nome1 = 'methanol'
    # nome1 = 'methyl'
    # nome1 = 'ethanol'
    # nome2 = 'methanol'
    # nome2 = 'ethanol'
    # nome2 = 'cloroform'
    # nome2 = 'benzene'
    # nome2 = 'methyl'
    # nome2 = 'ipropanol'
    # nome2 = 'npropanol'
    # nome2 = 'hexafluorobenzene'
    # nome2 = 'water'
    nome1, nome2, p = Catch_nome()
    nome_elem = [nome1, nome2]
    atm = p*101.325
    n = 2
    elem = [0]
    r = []
    T = indv['temp']
    for i in nome_elem:
        elem.append(Elemento(i))
    mistura = nome_elem[0]+'-'+nome_elem[1]
    for i in range(1, n+1, 1):
        # print('psat', Psat(T, elem[i]))
        # print('nrtl', Nrtl(mistura, indv, T, n, i))
        r.append(
            log(atm) - log(Psat(T, elem[i])) - log(Nrtl(mistura, indv, T, n, i)))
    r1 = r[0]
    r2 = r[1]
    return pow(r1, 2) + pow(r2, 2) + pow(((indv['frac_1']+indv['frac_2'])-1), 2)


# indv = {
    # 0: {'nome1': 'acetone', 'nome2': 'cloroform', 'temp': (181.16 + 273.15), 'frac_1': 0.318, 'frac_2': 1-0.318}, #acetone-cloroform 15.8atm
#    1: {'nome1': 'acetone', 'nome2': 'cloroform', 'temp': (65.26 + 273.15), 'frac_1': 0.361, 'frac_2': 1-0.361}, #acetone-cloroform 2 1atm
    # 2: {'nome1': 'acetone', 'nome2': 'methanol', 'temp': (155.37 + 273.15), 'frac_1': 0.286, 'frac_2': 1-0.286}, #acetone-methanol 15.8atm
#    3: {'nome1': 'acetone', 'nome2': 'methanol', 'temp': (55.56 + 273.15), 'frac_1': 0.784, 'frac_2': 1-0.784}, #acetone-methanol 2 1atm
#    4: {'nome1': 'benzene', 'nome2': 'ipropanol', 'temp': (71.83 + 273.15), 'frac_1': 0.588, 'frac_2': 1-0.588}, #benzene-ipropanol 1atm
    # 5: {'nome1': 'benzene', 'nome2': 'hexafluorobenzene', 'temp': (35.56 + 273.15), 'frac_1': 0.975, 'frac_2': 1-0.975}, #!benzene-hexafluorobenzene 0.2atm
    # 6: {'nome1': 'benzene', 'nome2': 'hexafluorobenzene', 'temp': (37.82 + 273.15), 'frac_1': 0.169, 'frac_2': 1-0.169}, #!benzene-hexafluorobenzene 2 0.2atm
#    7: {'nome1': 'benzene', 'nome2': 'npropanol', 'temp': (76.83 + 273.15), 'frac_1': 0.764, 'frac_2': 1-0.764}, #!benzene-npropanol 2 1atm
    # 8: {'nome1': 'cloroform', 'nome2': 'methanol', 'temp': (151.57 + 273.15), 'frac_1': 0.406, 'frac_2': 1-0.406}, #cloroform-methanol 15.8atm
#    9: {'nome1': 'cloroform', 'nome2': 'methanol', 'temp': (53.29 + 273.15), 'frac_1': 0.656, 'frac_2': 1-0.656}, #cloroform-methanol 2 1atm
#    10: {'nome1': 'cloroform', 'nome2': 'ethanol', 'temp': (59.26 + 273.15), 'frac_1': 0.847, 'frac_2': 1-0.847}, #cloroform-ethanol 1atm
#    11: {'nome1': 'ethanol', 'nome2': 'benzene', 'temp': (67.79 + 273.15), 'frac_1': 0.447, 'frac_2': 1-0.447}, #ethanol-benzene 1atm
#    12: {'nome1': 'ethanol', 'nome2': 'methyl', 'temp': (74.08 + 273.15), 'frac_1': 0.486, 'frac_2': 1-0.486}, #!ethanol-methyl 1atm
#    13: {'nome1': 'ethanol', 'nome2': 'water', 'temp': (78.28 + 273.15), 'frac_1': 0.952, 'frac_2': 1-0.952}, #!ethanol-water 1atm
#    14: {'nome1': 'methyl', 'nome2': 'water', 'temp': (73.39 + 273.15), 'frac_1': 0.657, 'frac_2': 1-0.657}, #!methyl-water 1atm
#    15: {'nome1': 'methanol','nome2': 'benzene','temp': (58.13 + 273.15), 'frac_1': 0.611, 'frac_2': 1-0.611} #!methanol-benzene 2 1atm
# }
# indv = {
#     1: {'nome1': 'cloroform', 'nome2': 'ethanol', 'temp': 353.32872935154927, 'frac_1': 0.04009031449138614, 'frac_2': 0.9599096855086139}
# }
# print(Azeo(indv[1]))