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
        x = str(vote.c) + "\n" + str(vote.n) + "\n" + str(vote.n_sqr)
        cursor.execute("INSERT INTO Liste_Votes VALUES(?)", (x,))
        connect.commit()
        
def getAllVotes() :
    votes=[]
    res = cursor.execute("SELECT * FROM Liste_Votes")
    connect.commit()
    res = list(res.fetchall())

    for x in res :
        print("BEFORE = \n" + "\n" + str(x))
        (first,) = x
        xc = mpz(first.split("\n")[0])
        xn = mpz(first.split("\n")[1])
        xn2 = mpz(first.split("\n")[2])
        r1 = paillier.PaillierCiphertext(xc, xn)
        r1.n_sqr = xn2

        votes.append(r1)
        print("AFTER = " + str(paillier.PaillierCiphertext(xc, xn2)))
        print(xn2)
    return votes
        

dbCreateTable()