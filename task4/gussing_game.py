import random


def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("=" * 40)
    print("      NUMBER GUESSING GAME")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!\n")

    while True:
        guess_input = input("Enter your guess: ").strip()

        # Validate input
        if not guess_input.isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_input)

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.\n")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.\n")
        elif guess > number_to_guess:
            print("Too high! Try again.\n")
        else:
            print("\n" + "=" * 40)
            print(f"🎉 Congratulations! You guessed it right!")
            print(f"The number was {number_to_guess}.")
            print(f"It took you {attempts} {'attempt' if attempts == 1 else 'attempts'}.")
            print("=" * 40)
            break


def main():
    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()