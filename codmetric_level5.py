import random

def Rock_Paper_Scissors(player_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    print(f"\nComputer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock':
        print("You win!" if computer_choice == 'scissors' else "You lose!")
    elif player_choice == 'paper':
        print("You win!" if computer_choice == 'rock' else "You lose!")
    elif player_choice == 'scissors':
        print("You win!" if computer_choice == 'paper' else "You lose!")
    else:
        print("Invalid input.")
while True:
    print("\n--- Rock Paper Scissors Game ---")
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    Rock_Paper_Scissors(player_choice)

    again = input("Play again? (yes/no): ").lower()
    if again != 'yes':
        print("Bye bye! Game over 💜")
        break


