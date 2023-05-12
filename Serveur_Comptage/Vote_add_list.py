
from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array
votes = []
def create_list_vote(nb_of_candidates) :
    votes = zeros(nb_of_candidates, int)
    return votes
def vote_add_List( votant , vote, votes) :
    votes.append((votant,vote))


