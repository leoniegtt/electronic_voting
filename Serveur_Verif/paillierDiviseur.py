from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros

#modular division to reveal number of votes for each candidate
def division(candidates, results, nb_of_candidates) :

    print("result----"+ str(results))
    #nb_of_candidates += 1

    candidate_votes = zeros(nb_of_candidates+1, mpz)
    candidate_votes[nb_of_candidates], _voting_results=f_divmod(results,mpz(candidates[nb_of_candidates]))
    print("Candidate " + str(nb_of_candidates+1) +" votes: {0}".format((candidate_votes[nb_of_candidates])))
    for i in range(nb_of_candidates-1 ,-1,-1):
        candidate_votes[i] , _voting_results = f_divmod(_voting_results,(candidates[i]))
        print("Candidate " + str(i+1) +" votes: {0}".format((candidate_votes[i])))
    