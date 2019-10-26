import random
import os
import sys
lst = []
lst_random = []
name_of_file = input("give the name of the file ")
min_value = input("give the min value ") 
max_value = input("give the max value ")
amount_of_numbers = input("give the amount of numbers ")
int_min_value = int(min_value)
int_max_value = int(max_value)
int_amount_of_numbers = int(amount_of_numbers)
for number in range(int_min_value,int_max_value+1):
    lst.append(number)
# print(lst[0])
# print(lst[-1])
for numberr in range(int_amount_of_numbers):
    lst_random.append(random.choice(lst))
file_path = os.path.dirname(os.path.realpath(__file__))+"\\"+name_of_file+".txt"
print(file_path)
txt_file = open(file_path,"w+")
for number in lst_random:
   txt_file.write(str(number)+";")
txt_file.close()

