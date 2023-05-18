import sqlite3

#import fonction marie qui donne

connect = sqlite3.connect("Serveur_Orga/dbb_orga.db")
cursor = connect.cursor()

#VERIFICATION QUE LES LOGIN, MDP ENTRES CORRESPONDENT A CEUX DE LA BDD

global token_local

def verifLogin(login):
        statement = f"SELECT login from Liste_Votant2 WHERE login='{login}';"
        cursor.execute(statement)
        if not cursor.fetchone():  # An empty result evaluates to False.
                # print("Login not exist : " + username)
                return False
        else:
                # print("Welcome " + username + " !")
                return True

def verifPwd(login, pwd):
        statement = f"SELECT login from Liste_Votant2 WHERE login='{login}' AND mdp = '{pwd}';"
        cursor.execute(statement)
        if not cursor.fetchone():  # An empty result evaluates to False.
                # print("Login failed " + username)
                return False
        else:
                # print("You are connected " + username + " !")
                global token_local
                token_local = getToken(login, pwd)
                return True

def getToken(login, pwd) :
        statement = f"SELECT Token from Liste_Votant2 WHERE login='{login}' AND mdp = '{pwd}';"
        cursor.execute(statement)
        res = cursor.fetchone()
        token = res[0]
        return token

def returnToken() :
        return token_local