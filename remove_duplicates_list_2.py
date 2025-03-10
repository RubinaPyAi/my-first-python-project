'''write a program to remove duplicates'from the list entered by the user'''
'''--can be done in two ways
      1.By using set
      2.By using the append method'''
#By using the append method
n1=eval(input("enter the list elements:"))
lst=list(n1)
print (lst)
my_list=[]
for i in lst:
    if i not in my_list:
        my_list.append(i)
print(my_list)
