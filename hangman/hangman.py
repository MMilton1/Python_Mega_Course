import random

word_list = [
    "aardvark",
    "baboon",
    "camel",
    "apple",
    "banana",
    "orange",
    "elephant",
    "giraffe",
    "ocean",
    "mountain",
    "friendship",
    "butterfly",
    "sunshine",
    "rainbow",
    "chocolate",
    "adventure",
    "holiday",
    "balloon",
    "garden",
    "whisper",
    "laughter",
    "treasure",
    "family"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
word_picked = random.choice(word_list)
print(word_picked)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
placeholder = ""
word_length = len(word_picked)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

user_guest = input("Guess a letter: ").lower()

display = ""

for letter in word_picked:
    if letter == user_guest:
        display += letter
    else:
        display += "_"
print(display)
