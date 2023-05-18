import sys
import os

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Orga")
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Comptage")
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Verif")

import Fsend as db
import chiffrementVote
import dbVotes
#serveur verif
import gestionDBToken
import replaceToken

def voteChiffre(candidate, public_key_paillier) :
    vote_chiffre = chiffrementVote.chiffrement_vote(public_key_paillier, candidate)
    return vote_chiffre

def vote():
    print("LE VOTE COMMENCE")
    validvote = False
    alreadyVoted = False 
    while not validvote :
        
        # récup la liste des candidats à partir de la bdd
        # normalement je récup aussi tout le reste => comment je le stocke ????
        [token,public_key_paillier, candidates, candidates_num] = db.sendtoVoter()
        token2 = replaceToken.getToken2(token)

        if token2 == "ERROR" :
            print("You have already voted.")
            print("You cannot vote again for this election. Goodbye.")
            validvote = True
            alreadyVoted = True
        else :
            print("Here are the candidates : ") 
            print(candidates)
            vote=int(input("Enter your vote (number from 0 to " + str(len(candidates_num)-1 )+") "))
            
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

    if not  alreadyVoted:
        # Envoyer le vote chiffré
        vote_chiffre_local = voteChiffre(candidates_num[vote], public_key_paillier)
        dbVotes.insertVote(vote_chiffre_local,token2)        
    
        print ("Your vote has been casted.")
        print("Here is your ballot: \n" + str(vote_chiffre_local)+ "\nYou can save it to verify your vote when the election is done!")
    