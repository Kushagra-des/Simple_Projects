import random 

print("|------ Welcome to the Game of ROCK, PAPER, SCISSORS ------|\n")
print("Rules: \n(1). Rock beats Scissors \n(2). Scissors beats Paper \n(3). Paper beats Rock\n")

options = ["rock","paper","scissors"]

user = input("Enter Your Choice for this Game: ").lower()

computer = random.choice(options)

print("Computer Chooses: ", computer)

# Tie case 
if user == computer:
    print("It is a Tie")

# User Win Cases
elif user == "rock" and computer == "scissors":
    print("User Win")
elif user == "paper" and computer == "rock":
    print("User Win")
elif user == "scissors" and computer == "paper":
    print("User Win")

# Computer Win Cases 
elif user == "scissors" and computer == "rock":
    print("Computer Win")
elif user == "rock" and computer == "paper":
    print("Computer Win")
elif user == "paper" and computer == "scissors":
    print("Computer Win")

# Invalid Case 
else:
    print("Invalid Input")