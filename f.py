import random

# Mapping for the game logic: 1=Rock, 0=Scissors, -1=Paper
you_dict = {"r": 1, "p": -1, "s": 0}
reverse_dict = {1: "Rock", 0: "Scissors", -1: "Paper"}

print("Welcome to Rock Paper Scissors!")

while True:
    computer = random.choice([-1, 0, 1])
    
    # Get user input inside the loop
    you_str = input("\nEnter your choice (r for Rock, p for Paper, s for Scissors) or type 'q' to quit: ").lower()

    if you_str == 'q':
        print("Thanks for playing! Exiting game.")
        break # This exits the while loop and stops the program

    if you_str not in you_dict:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        continue # This skips the rest of the loop and starts the next iteration

    you = you_dict[you_str]

    print(f"\nYou chose {reverse_dict[you]}")
    print(f"Computer chose {reverse_dict[computer]}")

    # Determine the winner using a simplified and correct logic for Snake Water Gun
    if computer == you:
        print("Game Draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        # Paper covers Rock (-1 vs 1), Scissors cuts Paper (0 vs -1), Rock crushes Scissors (1 vs 0)
        print("You Win!")
    else:
        print("You Lose!")
