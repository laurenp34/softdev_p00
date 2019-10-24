#Team Noobpedia: Raymond Lee, Kevin Li, Emory Walsh
#SoftDev1 pd1
#P00 -- Da Art of Storytellin'
#2019-10-28

from flask import Flask, render_template, request, redirect, url_for, session, flash
import os #for generating a secret key
from utl import db_ops

app = Flask(__name__)

#Secret key handling
secret_key_file = 'secret_key.txt'
if (os.path.exists(secret_key_file)): #check if secret key file already exists
    file = open(secret_key_file, 'r')
    app.secret_key = file.read()
else: #not adding the secret key file, so generate one on the spot for ppl without it
    file = open(secret_key_file, 'w+') #w+ creates the file if it doesn't exist
    file.write(str(os.urandom(32)))
    app.secret_key = file.read()

file.close()

@app.route("/")
def home():
    if 'user' in session: #checks that a user is logged into a session, render welcome page
        print("Session username: " + session['user'])
        return render_template("welcome.html")

    return render_template("login.html") #if not, then render login page

@app.route("/signup")
def signup():
    return render_template("register.html")

@app.route("/register", methods=['POST'])
def register():
    username = request.form.get('user')
    password = request.form.get('pw')

    # keep working on this
    # if not (username and password): 
    #     flash("Username or Password cannot be empty.")
    #     return redirect(url_for('register'))

    if (db_ops.accountExists(username)):
        return "This username is already in use. Try another one."

    db_ops.addAccount(username, password)
    return "Success!"

@app.route("/newstory", methods=['GET', 'POST'])
def newStory():
    if (session.get('user')): #checks that a user is logged into a session, render new story page
        return render_template("newstory.html")
    return render_template("newstory.html", error="Please log in first to create a new story.") # to check if user has logged in before letting them create a new story

@app.route("/auth", methods=['POST'])
def login():
    username = request.form.get('user')
    password = request.form.get('pw')

    if not (username and password):
            flash("Username or Password cannot be empty.")
            return redirect(url_for('checkLogin'))

    if (db_ops.authenticate(username, password)):
        return render_template("welcome.html")

    return "Incorrect username or password."

if __name__ == "__main__":
    app.debug = True
    app.run()

