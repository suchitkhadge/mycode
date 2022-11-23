#!/usr/bin/python3
from flask import Flask, redirect, url_for
import random

app = Flask(__name__)

quotes = ["I'm afraid for the calendar. Its days are numbered.",
"My wife said I should do lunges to stay in shape. That would be a big step forward.",
"Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!",
"Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
"What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.",
"What do you call a fish wearing a bowtie?" "Sofishticated.",
"How do you follow Will Smith in the snow?" "You follow the fresh prints.",
"If April showers bring May flowers, what do May flowers bring?" "Pilgrims.",
"I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along."]

@app.route("/quotes")
def hello_admin():
    return [random.choice(quotes)]


@app.route("/user/<name>")
def hello_user(name):
    ## if you go to hello_user with a value of admin
    if name =="admin":
        # return a 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("hello_guest",guesty = name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
 
