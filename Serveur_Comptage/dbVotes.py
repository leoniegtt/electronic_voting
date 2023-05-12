import sqlite3

from gmpy2 import mpz

from paillierlib import paillier

# Création fichier base de données .db
connect = sqlite3.connect("Serveur_Comptage/dbb_vote.db")
cursor = connect.cursor()

# Création des tables
def dbCreateTable():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_Votes (vote BLOB(800), PRIMARY KEY (vote))")
        
def insertVote(vote):
        x = str(vote.c) + "\n" + str(vote.n)
        cursor.execute("INSERT INTO Liste_Votes VALUES(?)", (str(x),))
        connect.commit()
        
def getAllVotes() :
    votes=[]
    res = cursor.execute("SELECT * FROM Liste_Votes")
    connect.commit()
    res = list(res.fetchall())
    print("----------------------------------------")
    print(res)
    for x in res :
        (first,) = x
        print("(((((((((((((((((((((((((((((----------------------------------------)))))))))))))))))))))))))))))")
        print(type(first))

        xc = mpz(first.split("\n")[0])
        xn = mpz(first.split("\n")[1])
        votes.append(paillier.PaillierCiphertext(xc, xn))

    return votes
        

dbCreateTable()
print(getAllVotes())