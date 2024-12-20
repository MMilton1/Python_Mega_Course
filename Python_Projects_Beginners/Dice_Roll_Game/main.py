import random

print("Welcome to the Dice Rolling Game!")
print(r'''
   _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
''')

#account for how many rolls a user has had
user_roll_count = 0

while True:
    # get user input to roll or not
    user_input = input("Roll the dice? (y/n):").lower()
    if user_input == 'y':
        user_roll_count += 1
        user_roll_count = int(input("How many dice do you roll?"))
        # Get the two random die rolls
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        for roll in range(0,user_roll_count):
            print(f"({die_1},{die_2})")
    elif user_input == 'n':
        print("Thanks for playing.")
        print(f"You rolled a {user_roll_count} times.")
        break
    else:
        print("Invalid input!")