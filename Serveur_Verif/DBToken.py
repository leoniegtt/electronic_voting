#executer une fois : python Serveur_Verif/DBToken.py
 

import sqlite3

# Création fichier base de données .db
connect = sqlite3.connect("Serveur_Verif/dbb_token.db")
cursor = connect.cursor()

# Création des tables
def dbCreateTables():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_Token (Token1 VARCHAR(300), Token2 VARCHAR(300), PRIMARY KEY (Token1))")


def insertTokens(token1, token2) :
        #à faire quand on reçoit le token du voter dans le bulletin de vote
        cursor.execute("INSERT INTO Liste_Token VALUES(?, ?)", (token1, token2))
        connect.commit()

def isTokenExists(token): #modif
        cursor.execute("SELECT * FROM Liste_Token WHERE Token=?", (token))
        res = cursor.fetchone()
        if res is None:
            print("*** Le token n'a jamais été utilisé pour voter : 1er vote ***")
            return True
        else:
            return False

def getListToken() : #pour le résultat
        res = cursor.execute("SELECT * FROM Liste_Token")
        connect.commit()
        res = list(res.fetchall())
        return res
        

dbCreateTables()