from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array

def generate_key ():
    key_pair = paillier.keygen()
    return key_pair
