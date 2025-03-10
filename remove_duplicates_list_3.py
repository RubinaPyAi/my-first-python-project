'''write a program to remove duplicates'from the list entered by the user'''

# By using the append method using function
def remove_dup(lst1):
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return(lst1)        
n1=eval(input("Enter the list elements: "))
lst=list(n1)
print(lst)
my_list=[]
res=remove_dup(my_list)
print("list after removing the duplicates is:",res)