#executer une fois : python Serveur_Verif/DBToken.py
 
import sqlite3

# Création fichier base de données .db
connect = sqlite3.connect("Serveur_Verif/dbb_token.db")
cursor = connect.cursor()

# Création des tables
def dbCreateTables():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_Token (Token1 VARCHAR(300), Token2 VARCHAR(300), Utilise INTEGER, PRIMARY KEY (Token1))")


def insertTokens(data_token1) :
        #à faire quand on reçoit le token du voter dans le bulletin de vote
        cursor.executemany("INSERT INTO Liste_Token VALUES(?, ?, ?)", data_token1)
        connect.commit()

def isTokenExists(token1): #0 : arrêt du vote, 1: première création token2, 2 : nouvelle création de token2
        cursor.execute("SELECT * FROM Liste_Token WHERE Token1=?", (token1, ))
        res = cursor.fetchone()
        if res is None: #pas de résultat, le token n'est pas inscrit, le voteur n'a pas les droits
                print("[syst] RETURN 1 (Le token1 n'est pas dans la base de donnée, vote interdit)")
                return 0
        else: #token1 déjà présent, un token2 a déja été créé
                print("[syst] Le token1 est dans la base de donnée")
                val_token2 = res[1]
                condition = res[2]
                if val_token2 == "0" :
                        print("[syst] RETURN 1 (le client n'a pas voté, première génération de token2)")
                        return 1
                else :     
                        if condition == 1 :
                                print("[syst] RETURN 0 (le client a déjà voté, arrêt du processus)")
                                return 0
                        else :
                                print("[syst] RETURN 2 (maj de token2)")
                                return 2

def isTokenUtilise(token2) :
        cursor.execute("SELECT Utilise FROM Liste_Token WHERE Token2=?", (token2, ))
        res = cursor.fetchone()
        if res[0] == 0 :
                print("[syst_verif] Le vote est accepté")
                #maj valeur utilisé à 1
                updateUtilise(token2)
                return True
        else :
                print("[syst_verif] Le vote est refusé")
                return False
        

def updateToken(token1, token2):
        cursor.execute("UPDATE Liste_Token SET Token2 = ? WHERE Token1 = ?", (token2, token1))
        connect.commit()

def updateUtilise(token2):
        cursor.execute("UPDATE Liste_Token SET Utilise = ? WHERE Token2 = ?", (1, token2))
        connect.commit()


def getListToken() : #pour le résultat
        res = cursor.execute("SELECT Token1 FROM Liste_Token")
        connect.commit()
        res = list(res.fetchall())
        return res
        

dbCreateTables()