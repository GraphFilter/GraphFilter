import os
from filter_list import FilterList
from src.backend.operations_and_invariants import bool_invariants as i_bool

file_in = open(os.path.abspath('resources/graphs/graphs7.g6'), 'r')
group = file_in.read().splitlines()

expression = input('Equation:')

ibool = i_bool.InvariantBool()
dic_inv_bool = {}
i = 0
for inv in ibool.all:
    dic_inv_bool[i] = inv.name
    i = i + 1

print(dic_inv_bool)
choice = input("Type the bool invariants:").split(",")
inv_choice = []
for i in range(0, len(choice)):
    inv_choice.append(ibool.all[int(choice[i])])

list_out, p = FilterList.run(group, expression=expression, list_inv_bool=inv_choice)
file_in.close()
print(p)
