import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Comptage")
import paillier_compteur

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Orga")
import dbVotes
import ClisteCandidats

from paillier_generate_key import get_key_pair
from decipher import decipher
from paillierDiviseur import division

def giveResults() :
    print("RESULTATS")
    votes = dbVotes.getAllVotes()
    print("\nNombre de bulletins de vote : " + str(len(votes)) + "\n")
    key_pair = get_key_pair()
    public_key = key_pair.public_key
    
   
    print("Voici la liste des bulletins de vote :")
     #pas donner la clé privée au compteur
    sum = paillier_compteur.compteur (votes,public_key)
    results = decipher(sum,key_pair)
    print("\nresultsss " + str(results))
    (c, candidates) = ClisteCandidats.transformCandidates(ClisteCandidats.getCandidates())
    print ("\nlen_candidate = " + str(len(candidates)-1))
    division(candidates , results, len(candidates)-1)

giveResults()