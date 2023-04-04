# vérifier l'idd du votant et qu'il a le droit de voter

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
                notconnected=False
            else:
                print("Mot de passe incorrect.")
                print("Mot de passe incorrect")
                
        else: 
            print("Vous n'êtes pas enregistré en tant que votant pour cette élection.")
            print("Essayez à nouveau.")


connexion()