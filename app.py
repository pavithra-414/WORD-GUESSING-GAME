from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

def load_words():
    with open("words.txt") as f:
        return f.read().splitlines()

# Global variables
word = random.choice(load_words())
guessed = []
attempts = 6

@app.route("/", methods=["GET", "POST"])
def home():
    global guessed, attempts, word

    message = ""
    hint = word[0]

    if request.method == "POST":
        guess = request.form["letter"].lower()

        if guess not in guessed:
            guessed.append(guess)
            if guess not in word:
                attempts -= 1

    display = " ".join([l if l in guessed else "_" for l in word])

    if "_" not in display:
        message = "🎉 You Won!"
    elif attempts == 0:
        message = f"💀 You Lost! Word was {word}"

    return render_template("index.html", display=display, attempts=attempts, message=message, hint=hint)

@app.route("/restart")
def restart():
    global guessed, attempts, word
    word = random.choice(load_words())
    guessed = []
    attempts = 6
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)