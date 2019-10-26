name_of_file = input("give the name of the file ")
file_path = "C:\\Users\\Kubaw\\Desktop\\coding\\Python\\elective\\FB homework\\"+name_of_file+".txt"
txt_file = open(file_path,"r+")
txt_data = str(txt_file.readline().strip(";"))
lst = []
sub_lst = []
for number in txt_data.split(";"):
    lst.append(int(number))
print(lst)
for number in lst:
    if number % 2 == 0 and number % 7 == 0:
        print("FB")
        lst[lst.index(number)] = "FB"
    elif number % 2 == 0:
        print("F")
        lst[lst.index(number)] = "F"
    elif number % 7 == 0:
        print("B")
        lst[lst.index(number)] = "B"
    else:
        print("NOT FB")
        lst[lst.index(number)] = "NOT FB"
txt_file.close()
print(lst)
ans_file_path = "C:\\Users\\Kubaw\\Desktop\\coding\\Python\\elective\\FB homework\\"+name_of_file+"_ans.txt"
ans_file = open(ans_file_path,"w+")
for string in lst:
    ans_file.write(str(string)+";")
ans_file.close()
