import random

words = ["apple", "banana", "grape", "mango", "orange"]
word = random.choice(words)

guessed = []
attempts = 6

print("🎮 Word Guessing Game")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You Won!")
        break

    guess = input("Enter letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("💀 You Lost! Word was:", word)