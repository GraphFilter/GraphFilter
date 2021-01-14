import os
from FilterTheList import Filter
from src.backend.Operations_and_Invariants import Invariant_bool as i_bool

file_In = open(os.path.abspath('matchingNumber5.g6'), 'r')
list = file_In.read().splitlines()

expression = input('Insira a (in)equação')

ibool = i_bool.Invariant_bool()
dic_inv_bool = {}
i = 0
for inv in ibool.all:
    dic_inv_bool[i] = inv.name
    i = i + 1

print(dic_inv_bool)
choice = input("Escolha quais condições deseja ativar na busca:").split(",")
inv_choice = []
for i in range(0, len(choice)):
    inv_choice.append(ibool.all[int(choice[i])])

list_out, p = Filter.Run(list, expression=expression, list_inv_bool=inv_choice)
file_In.close()
print(p)
