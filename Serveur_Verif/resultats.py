import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Comptage")
import paillier_compteur

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Orga")
import dbVotes
import ClisteCandidats

import paillier_generate_key
from decipher import decipher
from paillierDiviseur import division

def impressVote(votes):
    for index in range(len(votes)) :
        print("vote n° : " + str(index+1))
        print(str(votes[index].c)+str(votes[index].n))
        print("\n")

def giveResults() :
    print("+++ RESULTATS +++ ")
    votes = dbVotes.getAllVotes()
    print("\nNombre de bulletins de vote : " + str(len(votes)) + "\n")
    print("Voici la liste des bulletins de vote :")
    impressVote(votes)
    

    public_key = paillier_generate_key.getPublic()
    private_key = paillier_generate_key.getPrivate()
    
     #pas donner la clé privée au compteur
    sum = paillier_compteur.compteur (votes,public_key)
    
    results = decipher(sum,private_key)
    
    (candidates_name, candidates) = ClisteCandidats.transformCandidates(ClisteCandidats.getCandidates())
    print("----- RESULTATS DES VOTES -----")
    division(candidates, candidates_name, results, len(candidates)-1)
    
giveResults()