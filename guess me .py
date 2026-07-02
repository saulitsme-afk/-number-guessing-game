#import random
# welcome message
import random

print("welcome to the number guessing game !")
print("i'm thinking of a number between 1 and 100")
print("you have 5 chance to guess the correct number ")
# difficulty selection
print("please select the dofficulty level :")
print("level 1 : easy ")
print("level 2 : medium")
print("level 3 : hard")
level = int(input("please select the dificulty level :"))
# set chance
if level == 1:
    chance = 10
    print("Great! you have selected the easy level")
elif level  == 2:
    chance = 5
    print('Great! you have selected the medium level')
elif level == 3:
    chance = 3
    print('Great! you have selected the hard level')
else:
    print("sorry , that's not a vaild level")
    exit()
print(f"YOU HAVE {chance} chance to guess the correct number ")
print(" let's start the game !")
# ramdom number
secret_number = random.randint(1, 100)
# variable to check
guessed_corectly = False
#game loop
for attempt in range(1, chance + 1):
    print(f"\nAttempt {attempt} of {chance}")
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct!")
        guessed_corectly = True
        break
    elif guess > secret_number:
        print("too high!")
    else:
        print("too low")

# loop has ended — now check the outcome ONCE
if not guessed_corectly:
    print("\ngame over")
    print(f"the number I was thinking of is {secret_number}.")
else:
    print(f"you guessed it in {attempt} attempts!")




