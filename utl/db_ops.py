import sqlite3
from datetime import datetime

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
        db.close()
        rowCount += 1
        if (rowCount != 1):
            return false;

        return pw == row[1];

def viewStories():
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    #Titles list to be used in next loop
    titles = []
    c.execute("SELECT * FROM stories")
    for row in c:
        titles.append(row[0])

    latestUpdates = []
    for title in titles:
        c.execute(
        """
            SELECT * FROM storyUpdates
            WHERE title = (?)
            ORDER BY timestamp DESC
        """, (title,)
        )

        update = c.fetchone()
        arr = []
        arr.append(str(update[0]))
        arr.append(str(update[1]))
        arr.append(str(update[2]))
        latestUpdates.append(arr)

    db.close()  #close database
    return latestUpdates

def fetchContributedToStories(user):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    #Stories contributed to list to be used in next loop
    titles = []
    c.execute(
    """
        SELECT * FROM storyUpdates
        WHERE user = (?)
        GROUP BY title
        ORDER BY title DESC
    """, (user,)
    )

    for row in c:
        titles.append(str(row[0]))

    stories = {}
    for title in titles:
        c.execute(
        """
            SELECT * FROM storyUpdates
            WHERE title = (?)
            AND user = (?)
            ORDER BY timestamp ASC
        """, (title, user)
        )

        updates = []
        for update in c:
            updates.append(str(update[1]))

        stories[title] = updates

    db.close()  #close database
    return stories

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

    db.close()  #close database

    if (rowCount == 1):
        return True

    return False

def addStory(title, creator, update):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute("INSERT INTO stories VALUES (?, ?)", (title, creator))

    c.execute("INSERT INTO storyUpdates VALUES(?, ?, ?, ?)", (title, update, creator, datetime.now()))

    #==========================================================

    db.commit() #save changes
    db.close()  #close database

def addStoryUpdate(title, addition, user):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute("INSERT INTO storyUpdates VALUES (?, ?, ?)", (title, addition, user))

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

    #==========================================================

    db.close()  #close database

    return "a"
