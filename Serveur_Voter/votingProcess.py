import sys
import os

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Bdd")
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Comptage")
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Verif")
import paillier_generate_key
import assign_num_candidate 
import Fsend as db
import chiffrementVote
import dbVotes
import DBToken

#public_key_paillier = ""
#vote_chiffre_local = ""

def getPublicKeyPaillier() :
     public_key_paillier = paillier_generate_key.get_key_pair().public_key
     return public_key_paillier

def voteChiffre(candidate) :
    public_key_paillier = getPublicKeyPaillier()
    vote_chiffre = chiffrementVote.chiffrement_vote(public_key_paillier, candidate)
    return vote_chiffre

def vote():
    candidates = dict()
    candidates_num =[]
    print("LE VOTE COMMENCE")
    validvote = False
    while not validvote :
        print("Here are the candidates : ")
        # récup la liste des candidats à partir de la bdd
        # normalement je récup aussi tout le reste => comment je le stocke ????
        [token, publick_paillier, candidates_dico] = db.sendtoVoter()
        
        for i in range(0, len(candidates_dico) ) :
            (name , numbers) = candidates_dico[i]
            candidates[i] = name
            candidates_num.append(numbers)
            
        print(candidates)
        vote=int(input("Enter your vote (number from 0 to " + str(len(candidates_num)-1 )+")"))
        
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

                else: 
                    print("Invalid answer. Please enter y for yes and n for no.")
    
    # Envoyer le vote chiffré
       
        vote_chiffre_local = voteChiffre(candidates_num[vote])
        dbVotes.insertVote(vote_chiffre_local)
        
    #envoyer le token
        DBToken.insertToken(token)
    
    print ("Your vote has been casted. Goodbye.")
    
    

