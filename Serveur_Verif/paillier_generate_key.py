
from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array

key_pair = paillier.keygen()

def get_key_pair ():
    return key_pair
