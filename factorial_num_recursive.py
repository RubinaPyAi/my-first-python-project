# factorial of a number using recursive function

def fact(num):
    if num<2:
        return 1
    return num*fact(num-1)
num=int(input("Enter the no to calculate the factorial:"))
print("The factorial of ",num, "is:",fact(num))  

