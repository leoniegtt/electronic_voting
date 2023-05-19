from gmpy2 import mpz
from paillierlib import paillier

def compteur (votes,public_key_paillier):

    nb_votes=0
    #initialize the sum
    sum=paillier.encrypt(mpz(0), public_key_paillier)

    #initialize anonymous votes
    anon_votes=[]
    for ciphertext in votes:

        #print((ciphertext))
        # res=get_class(ciphertext[0])
        sum+=ciphertext
        anon_votes.append(ciphertext)
        nb_votes+=1

    somme_res = sum - paillier.encrypt(mpz(0), public_key_paillier)
    return somme_res
