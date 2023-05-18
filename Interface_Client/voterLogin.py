# Import the module0 directly since 
# the current path is of modules.
# import gestiondb as db
import votingProcess as vp
import sys
import os

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Orga")

import BverifLoginPwd as db

def getLoginInfo():
    login=input("Enter login : ")
    pwd=input("Enter password : ")
    return (login, pwd)

def connexion():
    print("Connexion au système de vote ALATAX : ")
    
    notconnected=True
    while notconnected:
        (login, pwd) = getLoginInfo()
        # vérif association correcte login password avec la bdd

        if db.verifLogin(login):
            if db.verifPwd(login, pwd):
                print("Connexion successful ! :)")
                #renvoyer sur la fonction du vote
                vp.vote()
                notconnected=False
            else:
                print("Mot de passe incorrect.")
                print("Essayez à nouveau.")    
        else: 
            print("Vous n'êtes pas enregistré en tant que votant pour cette élection.")
            print("Essayez à nouveau avec un login valide.")


connexion()