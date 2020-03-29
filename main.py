def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    return x/y

print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")

choice=int(input("enter your choice:"))
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))

if choice==1:
    print("sum is:",add(num1,num2))

elif choice==2:
    print("substraction is:",subtract(num1,num2))


elif choice==3:
    print("product is:",multiply(num1,num2))


elif choice==4:
    print("division is:",division(num1,num2))



else:
    print("INVALID CHOICE")
