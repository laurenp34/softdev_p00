import sqlite3

DB_FILE = "discobandit.db"

def accountExists(user):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute(
    """
        SELECT * FROM accounts WHERE username = (?)
    """, (user,)
    )

    rowCount = 0
    for row in c:
        rowCount += 1

    print(rowCount)

    #==========================================================

    db.commit() #save changes
    db.close()  #close database

    if (rowCount > 0):
        return True

    return False

def addAccount(user, pw):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute("INSERT INTO accounts VALUES (?, ?)", (user, pw))

    #==========================================================

    db.commit() #save changes
    db.close()  #close database


def addStory(title, creator):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute("INSERT INTO stories VALUES (?, ?)", (title, creator))

    #==========================================================

    db.commit() #save changes
    db.close()  #close database


def addStoryUpdate(title, textUpdate, user):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute("INSERT INTO storyUpdates VALUES (?, ?, ?)", (title, textUpdate, user))

    #==========================================================

    db.commit() #save changes
    db.close()  #close database
