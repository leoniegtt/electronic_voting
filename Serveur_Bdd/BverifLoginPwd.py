import sqlite3

connect = sqlite3.connect("dbb_pir.db")
cursor = connect.cursor()

#VERIFICATION QUE LES LOGIN, MDP ENTRES CORRESPONDENT A CEUX DE LA BDD
def getInformation() :
        exec("../..") #executer fonction du système Voter qui renvoie login, pwd et les retourner
        

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
        
def Verification(login, pwd) :
        if verifLogin(login) and verifPwd(login, pwd) :
                return True
        else :
                return False