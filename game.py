import random

def gameWin(computer,you):
    if computer == you:
        return None
    elif computer == "s":
        if you == "p":
            return True
        elif you == "c":
            return False
    elif computer == "p":
        if you == "c":
            return True
        elif you == "s":
            return False
    elif computer == "c":
        if you == "s":
            return True
        elif you == "p":
            return False

print("Computer turn : Stone(s) Paper(p) or scissor(c) ?")
randomNo = random.randint(1,3)
if randomNo == 1:
    computer = "s"
elif randomNo == 2:
    computer = "p"
elif randomNo == 3:
    computer = "c"

print(str(computer))

you = input("Your turn : Stone(s) Paper(p) or scissor(c) ? \n")

a = gameWin(computer,you)

if a == None:
    print("Game is Tie!")
elif a == True:
    print("You win!")
else:
    print("You Loose!")