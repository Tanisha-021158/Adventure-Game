name=input("Enter your name:")
print("Welcome ",name," to this adventure game!")

print("You need to choose a path! choose left or right...")
ch=input("Enter your choice[left/right]:").lower()

if ch=="left":
    print("You have reached a river.")
    ch=input("What do you want to do?[swim/walk on bridge]:").lower()
    if ch=="walk" or ch=="walk on bridge":
        print("Good choice!You win the game!")
    else:
        print("Wrong choice!You lose!")
elif ch=="right":
    print("You have reached an old broken bridge")
    ch=input("What do you want to do?[go back/proceed ahead]").lower()
    if ch=="go back":
        print("Good choice!You win!")
    else:
        print("Wrong choice!You lose!")
else:
    print("Wrong choice!")

