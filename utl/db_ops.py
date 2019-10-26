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
            return False

        return pw == row[1]

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
            ORDER BY timestamp ASC
        """, (title,)
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

    c.execute("INSERT INTO storyUpdates VALUES (?, ?, ?, ?)", (title, addition, user, datetime.now()))

    #==========================================================

    db.commit() #save changes
    db.close()  #close database

def fetchLatestUpdate(title):
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    c.execute(
    """
        SELECT * FROM storyUpdates
        WHERE title = (?)
        ORDER BY timestamp DESC
    """, (title,)
    )

    update = c.fetchone()
    db.close()  #close database
    return update

def searchStories(searchValue):
    stories = viewStories()
    # compare each title with search value and sort by edit distance
    levenshteinDistances = {}
    for el in stories:
        levenshteinDistances[editDistDP(str(searchValue), str(el[0]))] = el
        print(el[0] + ": " + str(editDistDP(str(searchValue), str(el[0]))))
    levenshteinDistances = {k: levenshteinDistances[k] for k in sorted(levenshteinDistances)}
    #sortedBySearchTitles = [value for (key, value) in sorted(levenshteinDistances.items())]
    print(levenshteinDistances)
    return levenshteinDistances.values()
    
# dynamic programming implementation of edit distance
def editDistDP(str1, str2): 
    m = len(str1)
    n = len(str2)
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 