
import random 

def user(name):
    
    secret_number = random.randint(1, 100)
    
    score = 0

    while True:

        guess = int(input("Guess Secret Number: "))

        if guess == secret_number:
            score += 1
            print("Right Answer")
            print(f"You Guess Secret Number in {score} guesses")
            break

        elif guess > secret_number:
            print(("Enter Lower Number"))
            score += 1

        elif guess < secret_number:
            print("Enter Greater Number ")
            score += 1

    return score             

name1 = input("Enter Your Name: ")
user1 = user(name1)
print(user1)

name2 = input("Enter Your Name: ")
user2 = user(name2)

if user1 < user2:
    print(f"{name1} Win And Score {user1} And {name2} Score {user2}")
elif user2 < user1:
    print(f"{name2} Win And Score  {user2} And {name1} Score {user1}")
else:
    print(f"Match Tie {name1}{user1} == {name2}{user2}")    