#executer une fois : python Serveur_Verif/DBToken.py
 

import sqlite3

# Création fichier base de données .db
connect = sqlite3.connect("Serveur_Verif/dbb_token.db")
cursor = connect.cursor()

# Création des tables
def dbCreateTables():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_Token (Token1 VARCHAR(300), Token2 VARCHAR(300), Utilise INTEGER, PRIMARY KEY (Token1))")


def insertTokens(token1, token2) :
        #à faire quand on reçoit le token du voter dans le bulletin de vote
        cursor.execute("INSERT INTO Liste_Token VALUES(?, ?, ?)", (token1, token2, 0))
        connect.commit()

def isTokenExists(token1): #0 : arrêt du vote, 1: première création token2, 2 : nouvelle création de token2
        cursor.execute("SELECT * FROM Liste_Token WHERE Token1=?", (token1, ))
        res = cursor.fetchone()
        if res is None: #pas de résultat
                print("[syst] RETURN 1 (Le token1 n'a jamais été rentré dans la base de donnée, première création de token2)")
                return 1
        else: #token1 déjà présent, un token2 a déja été créé
                print("[syst] Le token1 a déjà été rentré dans la base de donnée")
                condition = res[2]
                if condition == 1 :
                        print("[syst] RETURN 0 (le client a déjà voté, arrêt du processus)")
                        return 0
                else :
                        print("[syst] RETURN 2 (maj de token2)")
                        return 2

def updateToken(token1, token2):
        cursor.execute("UPDATE Liste_Token SET Token2 = ? WHERE Token1 = ?", (token2, token1))
        connect.commit()

def updateUtilise(): # a faire
        return any


def getListToken() : #pour le résultat
        res = cursor.execute("SELECT Token1 FROM Liste_Token")
        connect.commit()
        res = list(res.fetchall())
        return res
        

#dbCreateTables()
#insertTokens("thomas","coucou")
#print(str(isTokenExists("marie")))