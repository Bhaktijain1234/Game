import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result

def main():
    """Main function to play multiple rounds and track scores."""
    user_score = 0
    computer_score = 0

    while True:
        result = play_game()

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing! Final Score:")
    print(f"You {user_score} - {computer_score} Computer")

if __name__ == "__main__":
    main()
