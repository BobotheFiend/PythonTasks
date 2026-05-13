import random

def generate_question():
    return random.randint(1, 9), random.randint(1, 9)


while True:
    number_one, number_two = generate_question()

    while True:
        answer = int(input(f"How much is {number_one} times {number_two}? "))

        if answer == number_one * number_two:
            print("Very good!")
            break
        else:
            print("No. Please try again.")

    choice = input("Do you want to continue?(y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing")
        break
