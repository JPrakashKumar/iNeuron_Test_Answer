
# input_list =[0,0,0,0,0,0,1]
# input_list =[3,0,5,0,9,0,1]
# input_list =[0,0,9,5,1,0,1]
input_list =[0,3,4,7,4,9,1]


list_of_zero=[]
list_of_non_zero=[]
list_of_non_zero= input_list.copy()

for i in input_list:
    if i == 0:
        list_of_zero.append(i)
        list_of_non_zero.remove(i)
    else:
        list_of_non_zero
print(list_of_non_zero+list_of_zero)
