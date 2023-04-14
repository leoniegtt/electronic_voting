import sqlite3

# Création fichier base de données .db
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

data_candidats = [
      ('Eric', 'Alata'),
      ('Arthur', 'Bit-Mono'),
      ('Vincent', 'Migliore'),
      ('Vincent', 'Mahout'),
]


def insertVotants(data_mul):
        cursor.executemany("INSERT INTO Liste_votants VALUES(?, ?, ?, ?, ?)", data_mul)
        co.commit()
        
def insertCandidates(data_candidates) :
        cursor.executemany("INSERT INTO Liste_candidats VALUES(?, ?)", data_candidates)
        co.commit()



# TEST Verification mdp et login bons



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

# return dictionnary with key : number, first_name last_name
def getCandidates() :
        res = cursor.execute("SELECT * FROM Liste_candidats")
        co.commit()
        res = list(res.fetchall())
        
        res_dict = {}

        for i in range(len(res)) :
                aux = res[i]
                res_dict[i+1]= aux[0] + " " + aux[1]

        return res_dict
        
        
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