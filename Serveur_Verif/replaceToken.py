import generateToken2
import DBToken

def getToken2(token1) :
    token2 = generateToken2.totalEncryption(token1)
    DBToken.insertTokens(token1, token2)
    return token2

# faire fonction qui regarde si t1 déjà dans bdd et si oui alors génère un nouveau t2