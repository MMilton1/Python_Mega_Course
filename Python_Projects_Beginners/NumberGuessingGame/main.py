import random
import logo

random_number_between_1_and_100 = random.randint(1, 100)


print(logo.logo)

while True:
    try:
        user_guess = int(input("Guess the number between 1 and 100:"))

        if user_guess < random_number_between_1_and_100:
            print("Too low")
        elif user_guess > random_number_between_1_and_100:
            print("Too high")
        else:
            print("Correct! You guessed the correct number!")
            break
    except ValueError:
        print("Please enter a valid number")