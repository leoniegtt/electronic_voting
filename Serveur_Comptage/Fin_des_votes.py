
import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Verif")
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Orga")

from pailler_compteur import compteur
from paillier_generate_key import get_key_pair
from decipher import decipher
from pailler_compteur import division
import dbVotes
import ClisteCandidats

def main() :
    votes = dbVotes.getAllVotes()
    key_pair = get_key_pair()
    sum = compteur (votes,key_pair)
    results = decipher(sum,key_pair)
    print("\nresultsss " + str(results))
    (c, candidates_num) = ClisteCandidats.transformCandidates(ClisteCandidats.getCandidates())
    
    candidates = candidates_num
    print ("\nlen_candidate = " + str(len(candidates)-1))
    division(candidates , results, len(candidates)-1)


if __name__ == "__main__":
    main()