'''write a program to remove duplicates'from the list entered by the user'''
'''--can be done in two ways
      1.By using set
      2.By using the append method'''
# By using the set
n1=eval(input("enter the list elements:"))
lst=list(n1)
print (lst)
set1=set(lst)
print(set1)
my_list=list(set1)
print(my_list)

