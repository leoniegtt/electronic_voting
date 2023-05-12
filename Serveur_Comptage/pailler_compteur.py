

from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array
import sys

def division(candidates, results, nb_of_candidates) :
    candidate_votes = zeros(nb_of_candidates+1, int)
    candidate_votes[nb_of_candidates], _voting_results=f_divmod(results,(mpz(candidates[nb_of_candidates])))
    print("Candidate " + str(nb_of_candidates) +" votes: {0}".format((candidate_votes[nb_of_candidates])))
    for i in range(nb_of_candidates-1 ,0,-1):
        candidate_votes[i] , _voting_results = f_divmod(_voting_results,int(candidates[i]))
        print("Candidate " + str(i) +" votes: {0}".format(int(candidate_votes[i])))
    #modular division to reveal number of votes for each candidate

def compteur (votes,key_pair):
    nb_votes=0
    #initialize the sum
    sum=paillier.encrypt(mpz(0), key_pair.public_key)

    #initialize anonymous votes
    anon_votes=[]
    print("heeeer")
    print(votes)
    for ciphertext in votes:
        print(type(ciphertext))
        #print("Vote Ciphertext:\n\n{0}".format(int(ciphertext[0]).c))
       # res=get_class(ciphertext[0])
        sum+=ciphertext
        print("'''''''''''''''''")
        print(sum)
        #anon_votes.append(ciphertext[0])
        nb_votes+=1

    print("chiffre sum:  \n{0}".format(sum))
    return sum


