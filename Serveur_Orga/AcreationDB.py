import sqlite3
import DcreateToken

# Création fichier base de données .db
connect = sqlite3.connect("Serveur_Orga/dbb_orga.db")
cursor = connect.cursor()

# Création des tables
def dbCreateTables():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_votants (f_name VARCHAR(100), l_name VARCHAR(100), mail VARCHAR(100), login VARCHAR(100), mdp VARCHAR(100), PRIMARY KEY (login))")
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_candidats (f_name VARCHAR(100), l_name VARCHAR(100), PRIMARY KEY (f_name, l_name))")
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_Votant2 ( login VARCHAR(100), mdp VARCHAR(100), Token VARCHAR(300), PRIMARY KEY (login, Token))")

def addToken() :
        data = []
        res = cursor.execute("SELECT login, mdp FROM Liste_votants")
        connect.commit()
        res = list(res.fetchall())
        for i in res :
                login = i[0]
                pwd = i[1]
                data.append((login, pwd, DcreateToken.totalEncryption(login, pwd)))
        insertInfoToken(data)

def insertVotants(data_mul):
        cursor.executemany("INSERT INTO Liste_votants VALUES(?, ?, ?, ?, ?)", data_mul)
        connect.commit()

def insertCandidates(data_candidates) :
        cursor.executemany("INSERT INTO Liste_candidats VALUES(?, ?)", data_candidates)
        connect.commit()
        
def insertInfoToken(data):
        cursor.executemany("INSERT INTO Liste_Votant2 VALUES(?, ?, ?)", data)
        connect.commit()


# Init database : 
data = [
        ('Anuar', 'A', 'anuar@mail', 'aaa', 'aaamdp'),
        ('Amine', 'AM', 'amine@mail', 'ami', 'aaamdp'),
        ('Marie', 'M', 'marie@mail', 'marie', 'nana'),
        ('Sirine', 'C', 'sirine@mail', 'sissou', '15'),
        ('Léonie', 'G', 'leo@mail', 'leo', 'dijon4ever'),
        ('Thomas', 'CG', 'thomas@mail', 'ttt', 'thomdp'),
]

data_candidats = [
      ('Eric', 'A'),
      ('Vincent', 'M'),
      ('Paul', 'S'),
]

dbCreateTables()
insertVotants(data)
insertCandidates(data_candidats)
addToken()
