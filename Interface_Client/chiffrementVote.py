#pip install paillierlib

from gmpy2 import mpz
from paillierlib import paillier

def chiffrement_vote( public_key, candidate) :
    ciphertext=paillier.encrypt(mpz(candidate), public_key)
    return ciphertext
