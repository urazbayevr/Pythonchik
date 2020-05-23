import random

print("--------------------Oyin Bastalaaaddiii----------------------")
player1 = input("make your choose:")
player2 = random.choice(['r','s','p'])
print(player2)
def rock_paper(player1, player2):
    if (player1 == "r" and player2 == "p") or (player1 == "p" and player2 == "s") or (player1 == "s" and player2 == "r"):
        print("Lose!!")
    elif (player1 == "r" and player2 == "s") or (player1 == "s" and player2 == "p") or (player1 == "p" and player2 == "r"):
        print("Wiinnn!!")
    else:
        print("Draaawww!!!")


rock_paper(player1,player2)