
from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array

def generate_key ():
    key_pair = paillier.keygen()
    return key_pair

def main() :
    jey = generate_key().public_key
    print(jey)
    print("hh")
    return jey

if __name__ == "__main__" :
    print("rr")
    main()