from gmpy2 import f_divmod
from gmpy2 import mpz

from numpy import zeros

#modular division to reveal number of votes for each candidate
def division(candidates, candidates_name, results, nb_of_candidates) :

    candidate_votes = zeros(nb_of_candidates+1, mpz)
    
    candidate_votes[-1], _voting_results=f_divmod(results,mpz(candidates[nb_of_candidates]))
    
    print("Candidate " + str(nb_of_candidates)+ " : " + str(candidates_name[nb_of_candidates]) +", votes obtenus : {0}".format((candidate_votes[-1])))
    
    for i in range(nb_of_candidates-1 ,0,-1):
        candidate_votes[i] , _voting_results = f_divmod(_voting_results,(candidates[i]))
        print("Candidate " + str(i) + " : " + candidates_name[i] +", votes obtenus : {0}".format((candidate_votes[i])))
        
    #affichage vote blanc
    candidate_votes[0] , _voting_results = f_divmod(_voting_results,(candidates[0]))
    print("Blank vote : {0}".format((candidate_votes[0])))
    