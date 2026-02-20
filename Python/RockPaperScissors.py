import random

print("===== ROCK PAPER SCISSORS GAME =====")
print("Instructions:")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'exit' to quit the game.\n")

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your choice: ").lower()

    if user_choice == "exit":
        print("\nThanks for playing!")
        print("Final Score -> You:", user_score, "| Computer:", computer_score)
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.\n")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game Logic
    if user_choice == computer_choice:
        print("It's a tie!\n")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!\n")
        user_score += 1

    else:
        print("Computer wins this round!\n")
        computer_score += 1

    print("Current Score -> You:", user_score, "| Computer:", computer_score)
    print("-" * 40)

print("Game Over!")
