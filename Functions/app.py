# def greet(name):
#     print("Hello, " + name)
#     print("Lets learn Python Functions")
#
#
# greet("Murray")
#
#
# # Arguments
# def saySomething(age, current_year,  first_name, last_name):
#     date_of_birth = int(current_year - age)
#     print(f"Hello, {first_name } {last_name}! Your year of birth is {date_of_birth}")


# saySomething(33, 2024, "Murray", "Murray")

# Types of Functions

# 1 Functions that perform a task


# 2 Functions that return a value

# def get_age(age):
#     return f"You are {age} years old"
#
# user_age = get_age(33)
# file = open("content.txt", "w")
# file.write(user_age)



#
# def increment(number, by=4):
#     return number + by
#
# print(increment(2))
#
# # xargs vs xxargs
#
# def multiply(x, y):
#     return x * y





def divide(*numbers):
    total = 1
    for number in numbers:
        total /= number
    return total


print(divide(2,3,2,5))
