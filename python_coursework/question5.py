#Write a program to find numbers that are divisible by 4 and multiples of 6, between 2500 and 3800

pl=[]
for x in range (2500,3800):
    if (x%4==0)and (x%6==0):
        pl.append(str(x))
print (','.join(pl)) 