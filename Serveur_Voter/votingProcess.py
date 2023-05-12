import sys
import os

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Bdd")

import Fsend as db
import chiffrementVote

public_key_paillier = ""
vote_chiffre_local = ""

def getPublicKeyPaillier(publick_paillier) :
     public_key_paillier = publick_paillier

def voteChiffre(candidate) :
    vote_chiffre = chiffrementVote.chiffrement_vote(public_key_paillier, candidate)
    return vote_chiffre

def sendChiffre() : 
    return vote_chiffre_local

def vote():
    validvote = False
    while not validvote:
        print("Here are the candidates : ")
        # récup la liste des candidats à partir de la bdd
        # normalement je récup aussi tout le reste => comment je le stocke ????
        [token, publick_paillier, candidates] = db.sendtoVoter()
        getPublicKeyPaillier(publick_paillier)
        print(candidates)
        vote=int(input("Enter your vote (number from 1 to 4) : "))
        
        if vote not in candidates:
            print("Invalid vote. Please enter a valid number from 1 to 4.")
        else:
            print("You voted for", candidates[vote] + ".")
            invalid = True
            while invalid:
                # vérifier que c'est bien la personne pour qui on veut voter
                yorn = input("Are you sure about you vote? yes (y) or no (n) ")
                if yorn == "y":
                    validvote = True
                    invalid = False
                elif yorn == "n":
                    validvote = False
                    invalid = False
                else: 
                    print("Invalid answer. Please enter y for yes and n for no.")
    
    # Envoyer le vote chiffré
        vote_chiffre_local = voteChiffre(candidates[vote])
    #envoyer le token
    print ("Your vote has been casted. Goodbye.")

    

