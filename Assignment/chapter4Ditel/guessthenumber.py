import random

while True:
    number = random.randint(1, 1000)

    print("Guess my number between 1 and 1000 with the fewest guesses:")

    guess = None

    while guess != number:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print("Congratulations. You guessed the number!")

    play_again = input("Play again? (y/n): ").lower()

    if play_again != 'y':
        print("Thanks for playing!")
        break
