from paillierlib import paillier

def decipher (sum, private_key) :
    results = paillier.decrypt(sum, private_key)
    print("\nSomme déchiffrée du vote :\n{0}".format(results))
    print("\n")
    return results