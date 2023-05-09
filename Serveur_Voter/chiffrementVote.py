


from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array



def chiffrement_vote( public_key, candidate) :
    ciphertext=paillier.encrypt(mpz(candidate), public_key)
    return ciphertext