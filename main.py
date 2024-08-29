
print('''
1 - snake
-1 - water
0 - gun
''')
# Rules
"""Snake water gun game is a game which requires two players both have to select something
from snake or water or gun. snake wins over water , gun win over snake and water wins over gun
. ultimately the player with maximum points wins the game."""
import random
def game(me):
    computer = random.randint(-1,1)
    
    c_choose = {
        1:'snake',
        -1:'water',
        0:'gun'
    }

    youdic = {
        "snake":1,
        "water":-1,
        "gun":0
    }
    
    print(f"Computer Choose {c_choose[computer]}")
    user = youdic[me] # output is integer

    # Win conditions for the user
    if (computer == -1 and user == 1) or (computer == 0 and user == -1) or (computer == 1 and user == 0):
        print(f"User win!")

    # Lose conditions for the user
    elif (computer == 1 and user == -1) or (computer == -1 and user == 0) or (computer == 0 and user == 1):
        print(f"Computer wins!")

    # Tie condition
    elif computer == user:
        print("It's a tie!")

    else:
        print("Something went wrong")


me = input("Enter Your Player Name: ").lower()
game(me)
        