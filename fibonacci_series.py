# program to add the numbers of a fabonacci series
n=int(input("Enter the number: "))
a=0
b=1
print("Fabonacci series:")
for i in range(n):
    print(a ,end=",")
    temp=a
    a=b
    b=temp+b