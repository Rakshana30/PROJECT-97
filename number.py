import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a Number between 1-9")
while chances<5:
    guess = int(input("Enter your guess")) 
    if guess == number:
        print("Congratulations you won ")
    elif guess<number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")