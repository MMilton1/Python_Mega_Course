letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zeros = [0] * 100

numbers = list(range(1, 100 + 1))
chars = list("Hello World!")


char = []
for letter in letters:
    char.append(letter.upper())
print(letters[::-1]) #Reverse the list of the chars
print(char[::-1])


# list unpacking example
numbers2 = [1, 2, 3]
# first, second, third = numbers2
# print(first)

chars2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
first, second, *others2 = chars2
print(first)
# print(others)


dates = [23,19,1,6,7,9,20,22,30]
date1, date2, *others, last = dates
print(date1)
print(others)
print(last)


# Looping over a list
fruits = ['apple', 'banana', 'orange', 'strawberry']
for fruit in fruits:
    print(fruit)