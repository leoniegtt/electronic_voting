#pip install gmpy2==2.1.0rc1
#pip install paillierlib
from paillierlib import paillier

key_pair = paillier.keygen()

def get_key_pair ():
    return key_pair