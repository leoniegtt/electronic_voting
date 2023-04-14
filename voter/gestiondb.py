import sqlite3
co = sqlite3.connect("dbb_pir.db")
cursor = co.cursor()

# Création des tables
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

#cursor.executemany("INSERT INTO Liste_votants VALUES(?, ?, ?, ?, ?)", data)
#co.commit()



# TEST Verification mdp et login bons

username = "aaa"
password = "aaamdp"

def verifLogin(login):
        statement = f"SELECT login from Liste_votants WHERE login='{login}';"
        cursor.execute(statement)
        if not cursor.fetchone():  # An empty result evaluates to False.
                # print("Login not exist : " + username)
                return False
        else:
                # print("Welcome " + username + " !")
                return True

def verifPwd(login, pwd):
        statement = f"SELECT login from Liste_votants WHERE login='{login}' AND mdp = '{pwd}';"
        cursor.execute(statement)
        if not cursor.fetchone():  # An empty result evaluates to False.
                # print("Login failed " + username)
                return False
        else:
                # print("You are connected " + username + " !")
                return True

"""
verifLogin(username)
print("2°")
verifPwd(username, password)
"""