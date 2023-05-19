#pip install gmpy2==2.1.0rc1
#pip install paillierlib
from paillierlib import paillier
from gmpy2 import mpz

def chiffrement_vote( public_key, candidate) :
    ciphertext=paillier.encrypt(mpz(candidate), public_key)
    return ciphertext

def decipher (sum, private_key) :
    results = paillier.decrypt(sum, private_key)
    print("\nSomme déchiffrée du vote :\n{0}".format(results))
    print("\n")
    return results

def initKeyPaillier() :
    key_pair = paillier.keygen()
    
    public = key_pair.public_key
    pubn = public.n
    pubg = public.g
    
    private=key_pair.private_key
    pril = private.l
    priu = private.u
    prin = private.n
    
    with open("PubN.key", "w") as mykey:
        mykey.write(str(pubn))
    with open("PubG.key", "w") as mykey2:
        mykey2.write(str(pubg))
    with open("PriL.key", "w") as mykey3:
        mykey3.write(str(pril))
    with open("PriU.key", "w") as mykey4:
        mykey4.write(str(priu))
    with open("PriN.key", "w") as mykey5:
        mykey5.write(str(prin))

def getPublic() :
    with open("PubN.key", "r") as mykey:
        pubn = mpz(mykey.read())
        
    with open("PubG.key", "r") as mykey2:
        pubg = mpz(mykey2.read())
    
    publick = paillier.PaillierPublicKey(pubn, pubg)
    return publick

def getPrivate() :
    with open("PriL.key", "r") as mykey3:
        pril = mpz(mykey3.read())
    with open("PriU.key", "r") as mykey4:
        priu = mpz(mykey4.read())
    with open("PriN.key", "r") as mykey5:
        prin = mpz(mykey5.read())
    privatek = paillier.PaillierPrivateKey(pril, priu, prin)
    
    return privatek
