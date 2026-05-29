#------------------------  Task 1 ----------------------
import math
import math  # importing math module
import random  # importing random module
playing = True 
number = str(random.randint(0, 9)) 

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")

while playing:
  guess = input("Give me your best guess! \n")
  if number == guess:
    print("You win the game")
    print("The number was", number)
    break

  else:
    print("Your guess isn't quite right, try again. \n")

# ------------------------  Task 2 ----------------------

while True:  # iterate loop
    user_action = input(
        "Enter a choice (rock, paper, scissors): ")  # take input
    possible_actions = ["rock", "paper", "scissors"]
    # using random function
    computer_action = random.choice(possible_actions)
    # display both outputs what is selected by you and computer
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
# conditions to check who won the game
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
# take input for playing again
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break


# ------------------------  Task 3 ----------------------
# using ceil and floor functiom of math module
print('The Floor and Ceiling value of 23.56 are: ' +
      str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))

x = 10
y = -15
# using copysign function
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

# ------------------------  ACP ----------------------

# take input from user (in degrees)
angle = float(input("Enter angle in degrees: "))

# convert degrees to radians
radians = math.radians(angle)

# calculate values
sin_val = math.sin(radians)
cos_val = math.cos(radians)
tan_val = math.tan(radians)

# display results
print("Sin =", sin_val)
print("Cos =", cos_val)
print("Tan =", tan_val)
