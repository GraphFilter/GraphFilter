from src.backend.FilterTheList import Filter
import os

file_In = open(os.path.abspath('matchingNumber5.g6'),'r')
list=file_In.read().splitlines()
list_out, p = Filter.Run(list)
file_In.close()
print(p)