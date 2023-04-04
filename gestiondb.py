import sqlite3
co = sqlite3.connect("dbb_evote.db")
cursor = co.cursor()

cursor.execute ("CREATE TABLE IF NOT EXISTS Liste_votants (f_name VARCHAR(100), l_name VARCHAR(100), mail VARCHAR(100), login VARCHAR(100), mdp VARCHAR(100), PRIMARY KEY (login))")
cursor.execute("CREATE TABLE IF NOT EXISTS Liste_candidats (f_name VARCHAR(100), l_name VARCHAR(100), PRIMARY KEY (f_name, l_name))")
cursor.execute("CREATE TABLE IF NOT EXISTS Bulletins_vote (bulletin VARCHAR(100) PRIMARY KEY)")

data = [
        ('Anuar', 'A', 'anuar@mail', 'aaa', 'aaamdp'),
        ('Amine', 'AM', 'amine@mail', 'ami', 'aaamdp'),
        ('Marie', 'M', 'marie@mail', 'marie', 'nana'),
        ('Sirine', 'C', 'sirine@mail', 'sissou', '15'),
        ('Léonie', 'G', 'leo@mail', 'leo', 'dijon4ever'),
        ('Thomas', 'CG', 'thomas@mail', 'ttt', 'thomdp'),
]

cursor.executemany("INSERT INTO Liste_votants VALUES(?, ?, ?, ?, ?)", data)
co.commit()

# cursor.execute("SELECT mdp FROM Liste_votants WHERE login = ?")

# statement = f"SELECT login from Liste_votants WHERE login='{username}' AND mdp = '{password}';"
# cursor.execute(statement)
# if not cur.fetchone():  # An empty result evaluates to False.
#    print("Login failed")
# else:
#    print("Welcome")















