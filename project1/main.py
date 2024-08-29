import random
'''
-1 for water
1 for snake
0 for gun
'''

computer = random.choice([-1,0,1])
youStr = input("Enter your choice: ")
youDict = {    "s" : 1,    "w" : -1,    "g" : 0}
reverseDict = { -1 : "Water", 0: "Gun", 1: "Snake"}
you = youDict[youStr]

print(f"Your chose {reverseDict[you]}.\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

elif(computer == -1 and you == 1):
    print("You win")

elif(computer == -1 and you == 0):
    print("you lose")

elif(computer == 1 and you == -1):
    print("you lose")

elif(computer == 1 and you == 0):
    print("you Win")

elif(computer == 0 and you == -1):
    print("you win")

elif(computer == 0 and you == 1):
    print("you lose")
else:
    print("something went wrong")
