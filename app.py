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
    if ('user' in session): #checks that a user is logged into a session, render welcome page)
        #print("Session username: " + session['user'])
        flash ("You are logged in.")
        db_ops.fetchContributedToStories(session['user'])
        return render_template("welcome.html", title=db_ops.viewStory("Let it Go"))

    return render_template("login.html") #if not, then render login page

@app.route("/auth", methods=['POST'])
def login():
    username = request.form.get('user')
    password = request.form.get('pw')

    if (db_ops.authenticate(username, password)):
        session['user'] = username
        return redirect(url_for('home'))

    flash("Failed to log in. The username or password provided did not match any accounts.");
    return redirect(url_for('home'));

@app.route("/signup")
def signup():
    return render_template("register.html")

@app.route("/register", methods=['POST'])
def register():
    username = request.form.get('user')
    password = request.form.get('pw')

    if (db_ops.accountExists(username)):
        flash("This username is already in use. Try another one.")
        return redirect(url_for('signup'))

    db_ops.addAccount(username, password)
    flash("You have successfully created your account. Please log in now.")
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    session.pop('user') #logs the user out of the session
    flash("You have been logged out.")
    return redirect(url_for('home'))

@app.route("/create")
def create():
    return render_template("newstory.html")

#For the purposes of this program, considering the initial story as the first "update".
@app.route("/addstory", methods=['POST'])
def addStory():
    title = request.form.get('title')
    update = request.form.get('update')

    if (not db_ops.storyExists(title)):
        db_ops.addStory(title, session['user'], update)
        return "Story added to database, although you won't be able to access it via the website."

    return "Story exists, tough luck."

@app.route("/stories")
def stories():
    stories = db_ops.viewStories()
    return render_template("stories.html", stories=stories)

if __name__ == "__main__":
    app.debug = True
    app.run()
