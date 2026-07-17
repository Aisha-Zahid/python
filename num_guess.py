import random

name = input("Enter your name: ")
print("Welcome", name)

play = "yes"

while play.lower() == "yes":
    number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts = attempts + 1

        if guess == number:
            print("Correct! 🎉")
            print("Attempts:", attempts)
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

    play = input("Play again? (yes/no): ")

print("Thanks for playing!")