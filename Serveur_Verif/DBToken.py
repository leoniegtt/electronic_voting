import sqlite3

# Création fichier base de données .db
connect = sqlite3.connect("dbb_pir.db")
cursor = connect.cursor()

# Création des tables
def dbCreateTables():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_Token (Token VARCHAR(300), PRIMARY KEY (Token))")


def insertToken(token) :
        cursor.execute("INSERT INTO Liste_Token VALUES(?)", (str(token),))
        connect.commit()

def isTokenExists(token):
        cursor.execute("SELECT * FROM Liste_Token WHERE Token=?", (str(token),))
        res = cursor.fetchone()
        if res is None:
            insertToken(token)
            return True
        else:
            return False

def getListToken() :
        res = cursor.execute("SELECT * FROM Liste_Token")
        connect.commit()
        res = list(res.fetchall())
        return res
        

