#Write a python program that prompts a user to enter the bill to be paid at a restaurant and tip paid.
 #Then calculate how much each person paid and the total amount that was paid. 
 #Hint (You can also ask the user how many people were present.) Round the answers to 2dps

bill=float(input("please enter ammount paid: "))
tip=float(input("please enter the tip paid: "))
numPeople=int(input("please enter number of people: "))
total=(bill+tip)
ammount_per_person=float(total/numPeople)
print(" the total is: ", round(total,2))
print(" the amount paid per person is:",round(ammount_per_person,2))