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

    #==========================================================

    db.commit() #save changes
    db.close()  #close database

    if (rowCount == 1):
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

def authenticate(user, pw):
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
        if (rowCount != 1):
            return false;

        return pw == row[1];

def storyExists(title):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute(
    """
        SELECT * FROM stories WHERE title = (?)
    """, (title,)
    )

    rowCount = 0
    for row in c:
        rowCount += 1

    #==========================================================

    db.commit() #save changes
    db.close()  #close database

    if (rowCount == 1):
        return True

    return False

def addStory(title, creator, update):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute("INSERT INTO stories VALUES (?, ?)", (title, creator))

    c.execute("INSERT INTO storyUpdates VALUES(?, ?, ?)", (title, update, creator))

    #==========================================================

    db.commit() #save changes
    db.close()  #close database

def viewStory(title):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute(
    """
        SELECT * FROM stories WHERE title = (?)
    """, (title,)
    )

    for row in c:
        print(row)

    #==========================================================

    db.commit() #save changes
    db.close()  #close database

    return row[0]

def addStoryUpdate(title, textUpdate, user):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute("INSERT INTO storyUpdates VALUES (?, ?, ?)", (title, textUpdate, user))

    #==========================================================

    db.commit() #save changes
    db.close()  #close database
