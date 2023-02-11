#Martha is trying to login to her Gmail account to access some information. Write a program that authenticates and ensures 
#that the person logging in is Martha. (Hint-- use an if else statement)"""

userName=input("please enter user name: ")
password=input("password: ")
if userName=="Martha" and password=="martha22":
    print("login succesful ")
else:
    print("please enter correct username or password ")