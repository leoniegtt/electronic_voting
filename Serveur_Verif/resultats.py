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
    votes = dbVotes.getAllVotes()
    key_pair = get_key_pair()
    sum = paillier_compteur.compteur (votes,key_pair)
    results = decipher(sum,key_pair)
    print("\nresultsss " + str(results))
    (c, candidates_num) = ClisteCandidats.transformCandidates(ClisteCandidats.getCandidates())
    
    candidates = candidates_num
    print ("\nlen_candidate = " + str(len(candidates)-1))
    division(candidates , results, len(candidates)-1)

giveResults()