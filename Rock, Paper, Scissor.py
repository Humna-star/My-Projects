import random #Importing Random

while True:
    user_action = input("Enter a Choice (Rock, Paper, Scissor):")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print(f"\nYou choose{user_action}, computer choose{computer_action}.\n")

    if computer_action == user_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("Rock smatshes scissor, You win!")
        else:
            print("Paper covers rock, You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper cover rock, You win!")
        else:
            print("Scissor cut paper, You lose!")
    elif user_action == "Scissor":
        if computer_action == "paper":
            print("Scissor cuts paper, You win!")
        else:
            print("Rock smatcher scissor, You lose!")

    play_again = input("Play Again (y/n):")
    if play_again != "y":
        break
    