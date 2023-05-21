import generateToken2
import gestionDBToken as gestionDBToken

def getToken1(l_token):
    res = []
    for t1 in l_token :
        res.append((t1, 0, 0))
    gestionDBToken.insertTokens(res)

def getToken2(token1) :
    res = gestionDBToken.isTokenExists(token1)
    if (res == 0) :
        #arrêt processus
        return "ERROR"
    elif (res == 1):
        #Le token1 n'a jamais été rentré dans la base de donnée, première création de token2
        token2 = generateToken2.totalEncryption(token1)
        gestionDBToken.updateToken(token1, token2)
        return token2
    elif (res == 2) :
        #token1 déjà dans la bdd, mise à jour de token2
        token2 = generateToken2.totalEncryption(token1)
        gestionDBToken.updateToken(token1, token2)
        return token2
