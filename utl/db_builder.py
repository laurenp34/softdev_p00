import sqlite3

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================


#Initialize the accounts table
create_accounts_table = """ CREATE TABLE IF NOT EXISTS accounts (
                            username TEXT, password TEXT
                            );"""

c.execute(create_accounts_table)

def addAccount(user, pass):
    insert_account = str.format("INSERT INTO accounts VALUES ('{}', '{}');", user, pass)
    c.execute(insert_account)


#Initialize the stories table
create_stories_table = """ CREATE TABLE IF NOT EXISTS stories (
                           title TEXT, creator TEXT
                           );"""

c.execute(create_stories_table)

def addStory(title, creator):
    insert_new_story = str.format("INSERT INTO stories VALUES ('{}', '{}');", title, creator)
    c.execute(insert_new_story)

#Initialize the story updates table
create_updates_table = """ CREATE TABLE IF NOT EXISTS storyUpdates (
                           textUpdate TEXT, user TEXT
                           );"""

c.execute(create_updates_table)

def addUpdate(textUpdate, user):
    insert_new_update = str.format("INSERT INTO storyUpdates VALUES ('{}', '{}');", textUpdate, user)
    c.execute(insert_new_update)


#==========================================================

db.commit() #save changes
db.close()  #close database
