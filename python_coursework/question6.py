#question 6
n=int(input("enter number of lines: "))
for x in range(0,n):
    for x1 in range(0,x+1):
        print("*",end='')
    print()

for x in range(n,1,-1):
    for x1 in range(1,x):
        print("*",end='')
    print()