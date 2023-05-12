#pip install gmpy2==2.1.0rc1
#pip install paillierlib

from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array

key_pair = paillier.keygen()

def get_key_pair ():
    return key_pair

def main() :
    print("on est dans le main")
    
if __name__ == "__main__":
    main()