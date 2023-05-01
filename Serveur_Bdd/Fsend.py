import EverifLogin
import DcreateToken
import ClisteCandidats

#envoie token chiffré avec login, pwd, clé publique Pailler + la liste des votants
#question : est ce qu'on chiffre la clé publique pailler ? non je pense

def createListReturn(login, pwd) :
    token = DeprecationWarning.totalEncryption(login, pwd)
    publick_paillier = EverifLogin.returnPublicKeyPaillier
    dictCandidats = ClisteCandidats.getCandidates()
    res=[token, publick_paillier, dictCandidats]
    return res

def sendtoVoter() :
    if EverifLogin.checkLoginOK() :
        return createListReturn
    else : 
        return []

