from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros

def compteur (votes,public_key_paillier):

    nb_votes=0
    #initialize the sum
    sum=paillier.encrypt(mpz(0), public_key_paillier)

    #initialize anonymous votes
    anon_votes=[]
    for ciphertext in votes:

        print((ciphertext))
       # res=get_class(ciphertext[0])
        sum+=ciphertext
        anon_votes.append(ciphertext)
        nb_votes+=1

    print("chiffre sum: \n{0}".format(sum))
    return sum
