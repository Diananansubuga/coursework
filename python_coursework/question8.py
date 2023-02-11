#Write a program to convert temperature from Celsius to Fahrenheit and vice versa.

Fahrenheit=float(input("enter tempreture in  Fahrenheit: "))
celsius=(5/9)*( Fahrenheit -32)
print("the tempreture in celsius is: ",round(celsius,2))

celsius=float(input("enter tempreture in clesius: "))
Fahrenheit=(celsius*9/5)+32
print("the tempreture in Fahrenheit is: ",round(Fahrenheit,2))