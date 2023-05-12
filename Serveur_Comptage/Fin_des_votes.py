
import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Verif")
sys.path.append(os.path.dirname(__file__) + "/../Serveur_Bdd")
from pailler_compteur import compteur
from paillier_generate_key import get_key_pair
from decipher import decipher
from pailler_compteur import division
import dbVotes
import Fsend as db
def main() :
    votes = dbVotes.getAllVotes()
    key_pair = get_key_pair()
    sum = compteur (votes,key_pair)
    results = decipher(sum,key_pair)
    [token, publick_paillier, candidates_dico] = db.sendtoVoter()
    candidates = dict()
    candidates_num =[]
    for i in range(0, len(candidates_dico) ) :
        (name , numbers) = candidates_dico[i]
        candidates[i] = name
        candidates_num.append(int(numbers))

    candidates = candidates_num

    division(candidates , results, len(candidates)-1)



if __name__ == "__main__":
    main()

