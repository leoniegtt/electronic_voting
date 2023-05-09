from paillierlib import paillier
from gmpy2 import mpz
from Pailler import *

def cipher(candidate):
    key = get_public_key()
    cipher=paillier.encrypt(mpz(candidate),key)
    
    print("création du chiffré")

