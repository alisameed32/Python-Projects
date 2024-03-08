from flask import Flask
from brain import *
import time


computer_guess = 0

def low():
    return '<h1 style="color:red;"> Too low, try again!</h1>' \
           '<img src="https://i.giphy.com/jD4DwBtqPXRXa.webp"> '


def high():
    return ' <h1 style="color:purple">Too hogh, try again!</h1>' \
           '<img src="https://i.giphy.com/3o6ZtaO9BZHcOjmErm.webp"> '


def found():
    return ' <h1 style="color:green">You found me!</h1>' \
           '<img src="https://i.giphy.com/4T7e4DmcrP9du.webp"> '


app = Flask(__name__)

@app.route('/')
def start():
    global computer_guess 
    computer_guess = guessNum()
    return ' <h1 >Guess a number between 0 and 9 </h1>' \
           '<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp"> ' 


@app.route('/<int:number>')
def guess(number):
    
    
    if number<computer_guess:
        return low()
    elif number>computer_guess:
        return high()
    else:
        return found()        


if __name__ == "__main__":
    app.run(debug=True)

