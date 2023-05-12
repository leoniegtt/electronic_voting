import sqlite3

# Création fichier base de données .db
connect = sqlite3.connect("Serveur_Comptage/dbb_vote.db")
cursor = connect.cursor()

# Création des tables
def dbCreateTable():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_Votes (vote BLOB(800), PRIMARY KEY (vote))")
        
def insertVote(vote):
        cursor.execute("INSERT INTO Liste_Votes VALUES(?)", (str(vote),))
        connect.commit()
        
def getAllVotes() :
    res = cursor.execute("SELECT * FROM Liste_Votes")
    connect.commit()
    res = list(res.fetchall())        
    return res
        

dbCreateTable()
print(getAllVotes())