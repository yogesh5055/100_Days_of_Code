from flask import Flask
from random import randint

n = randint(0,9)
app = Flask(__name__)

@app.route("/")
def start():
    return "<h1>Guess a number between 0 and 9</h1>"\
              "<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/> "



@app.route("/<int:number>")
def check(number):
    if number==n:
        return "<h1 style='color:green;'>You found me!</h1>"\
        "<img src=' https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif number>n:
         return "<h1 style='color:blue;'>Too High,Try Again!</h1>"\
        "<img src=' https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
         return "<h1 style='color:red;'>Too Low,Try Again!</h1>"\
        "<img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"



if __name__ == "__main__":
    app.run(debug=True)
