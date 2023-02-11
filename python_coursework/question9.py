#Write a simple calculator program.
def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

operator=input("please choose option 1,2,3 or 4: ")
num1=int(input("enter any number: "))
num2=int(input("enter second number: "))

if operator=='1':
    print(add(num1,num2))
elif operator=='2':
    print(subtract(num1,num2))
elif operator=='3':
    print(multiply(num1,num2))
elif operator=='4':
    print(divide(num1,num2))







