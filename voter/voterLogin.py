# vérifier l'idd du votant et qu'il a le droit de voter
import votingProcess as vp

def connexion():
    print("Connexion au système de vote ALATAX : ")
    
    notconnected=True
    while notconnected:
        login=input("Enter login : ")
        pwd=input("Enter password : ")
        # vérif association correcte login password avec la bdd
        if login=="admin":
            if pwd=="admin123":
                print("Connexion successful ! :)")
                #renvoyer sur la page du vote // fonction du vote
                vp.vote()
                notconnected=False
            else:
                print("Mot de passe incorrect.")
                print("Essayez à nouveau.")
                
        else: 
            print("Vous n'êtes pas enregistré en tant que votant pour cette élection.")
            print(".")


connexion()