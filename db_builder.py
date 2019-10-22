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


#Initialize the stories table
create_stories_table = """ CREATE TABLE IF NOT EXISTS stories (
                           title TEXT, creator TEXT
                           );"""

c.execute(create_stories_table)

#Initialize the story updates table
create_updates_table = """ CREATE TABLE IF NOT EXISTS storyUpdates (
                           textUpdate TEXT, user TEXT
                           );"""

c.execute(create_updates_table)
#==========================================================

db.commit() #save changes
db.close()  #close database
