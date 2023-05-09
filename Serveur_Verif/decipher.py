

from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array

def decipher (sum, key_pair) :
    #decryption (TO DO : move to different file later)
    results = paillier.decrypt(sum, key_pair.private_key)
    print("vote results:\n{0}".format(results))
    return results