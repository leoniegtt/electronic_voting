

from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array

def compteur (votes,key_pair):
    nb_votes=0
    #initialize the sum
    sum=paillier.encrypt(mpz(0), key_pair.public_key)
    #initialize anonymous votes
    anon_votes=[]
    for voter,candidate in votes:
        print("Voter: {0}".format(voter))
        ciphertext=paillier.encrypt(mpz(candidate), key_pair.public_key)
        print("Vote Ciphertext:\n\n{0}".format(ciphertext.c))
        sum+=ciphertext
        anon_votes.append(ciphertext)
        nb_votes+=1
    print("chiffre sum:  \n{0}".format(sum))
    return sum