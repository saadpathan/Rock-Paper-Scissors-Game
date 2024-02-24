#rock paper scissors game

import random

while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        print("\n")
        player = input("rock, paper, or scissors ? : ").lower()

    if player == computer:
        print("Computer : ", computer)
        print("Player : ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You lose!")

        if computer == "scissors":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You lose!")

        if computer == "paper":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You lose!")

        if computer == "rock":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You win!")

    play_again = input("Do you want to play again ? (yes/no) : ").lower()
    print()

    if play_again != "yes":
        break

print("Game Over!")
print("Byeeeeeeeeeeeee!\n")



