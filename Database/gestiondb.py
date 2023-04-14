import sqlite3

# Création fichier base de données .db
def dbCreateFile():
        co = sqlite3.connect("dbb_pir.db")

cursor = co.cursor()

# Création des tables
def dbCreateTables():
        cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_votants (f_name VARCHAR(100), l_name VARCHAR(100), mail VARCHAR(100), login VARCHAR(100), mdp VARCHAR(100), PRIMARY KEY (login))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Liste_candidats (f_name VARCHAR(100), l_name VARCHAR(100), PRIMARY KEY (f_name, l_name))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Bulletins_vote (bulletin VARCHAR(100) PRIMARY KEY)")

# TEST en insérant dans la database : 

data = [
        ('Anuar', 'A', 'anuar@mail', 'aaa', 'aaamdp'),
        ('Amine', 'AM', 'amine@mail', 'ami', 'aaamdp'),
        ('Marie', 'M', 'marie@mail', 'marie', 'nana'),
        ('Sirine', 'C', 'sirine@mail', 'sissou', '15'),
        ('Léonie', 'G', 'leo@mail', 'leo', 'dijon4ever'),
        ('Thomas', 'CG', 'thomas@mail', 'ttt', 'thomdp'),
]

def insertTest(data_mul):
        cursor.executemany("INSERT INTO Liste_votants VALUES(?, ?, ?, ?, ?)", data_mul)
        co.commit()



# TEST Verification mdp et login bons

username = "aaa"
password = "aaamdp"


statement = f"SELECT login from Liste_votants WHERE login='{username}' AND mdp = '{password}';"
cursor.execute(statement)
if not cursor.fetchone():  # An empty result evaluates to False.
        print("Login failed")
else:
        print("Welcome " + username + " !")