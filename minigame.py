import random

wins = 0
losses = 0

rps = ["rock", "paper", "scissors"]
print("welcome to the mini game cove. choose your game \n 1. rock paper scissors")

choice = int(input("Enter number: "))

if choice == 1:
    print("Welcome to the rock paper scissors minigame to play just type your chosen move.")
while choice == 1:
    move = input("rock paper scissor shoot \n you: ")
    cmove = random.choice(rps)
    print("computer: ", cmove)

    if move == cmove:
        print("its a draw")
        print("Wins: ", wins,"  Losses: ",losses)
    elif move == "scissors" and cmove == "paper" or move == "paper" and cmove == "rock" or move == "rock" and cmove == "paper":
        wins = wins + 1
        print("congratulations you won")
        print("Wins: ", wins,"  Losses: ",losses)
    else:
        losses = losses + 1
        print("you lost")
        print("Wins: ", wins,"  Losses: ",losses)
