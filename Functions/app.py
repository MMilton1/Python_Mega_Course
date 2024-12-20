def save_user(**user_data):
    for key, value in user_data.items():
        print(value)

save_user(first_name="John", last_name="Smith", email="<john.smith@uyuu.com>", password="<PASSWORD>")

def fizz_buzz(*numbers):
    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print("Buzz")

fizz_buzz(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)