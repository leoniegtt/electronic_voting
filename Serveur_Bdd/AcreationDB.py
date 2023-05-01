import sqlite3

# Création fichier base de données .db
connect = sqlite3.connect("dbb_pir.db")
cursor = connect.cursor()

# Création des tables
def dbCreateTables():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_votants (f_name VARCHAR(100), l_name VARCHAR(100), mail VARCHAR(100), login VARCHAR(100), mdp VARCHAR(100), PRIMARY KEY (login))")
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_candidats (f_name VARCHAR(100), l_name VARCHAR(100), PRIMARY KEY (f_name, l_name))")

# TEST en insérant dans la database : 
data = [
        ('Anuar', 'A', 'anuar@mail', 'aaa', 'aaamdp'),
        ('Amine', 'AM', 'amine@mail', 'ami', 'aaamdp'),
        ('Marie', 'M', 'marie@mail', 'marie', 'nana'),
        ('Sirine', 'C', 'sirine@mail', 'sissou', '15'),
        ('Léonie', 'G', 'leo@mail', 'leo', 'dijon4ever'),
        ('Thomas', 'CG', 'thomas@mail', 'ttt', 'thomdp'),
]

data_candidats = [
      ('Eric', 'Alata'),
      ('Arthur', 'Bit-Mono'),
      ('Vincent', 'Migliore'),
      ('Vincent', 'Mahout'),
]

def insertVotants(data_mul):
        cursor.executemany("INSERT INTO Liste_votants VALUES(?, ?, ?, ?, ?)", data_mul)
        connect.commit()

def insertCandidates(data_candidates) :
        cursor.executemany("INSERT INTO Liste_candidats VALUES(?, ?)", data_candidates)
        connect.commit()
        
# Test :

"""
username = "aaa"
password = "aaamdp"
verifLogin(username)
print("2°")
verifPwd(username, password)
print(getCandidates())
#insertCandidates(data_candidats)
"""