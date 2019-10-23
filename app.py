#Team Noobpedia: Raymond Lee, Kevin Li, Emory Walsh
#SoftDev1 pd1
#P00 -- Da Art of Storytellin'
#2019-10-28

from flask import Flask, render_template, request, redirect, url_for, session
import os #for generating a secret key

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
    if (session.get('user')): #checks that a user is logged into a session, render welcome page
        print("Session username: " + session['user'])
        return "You are currently logged in!"

    return render_template("login.html"); #if not, then render login page

if __name__ == "__main__":
    app.debug = True
    app.run()
