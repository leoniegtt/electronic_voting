import EverifLogin
import BverifLoginPwd
import ClisteCandidats

#envoie token chiffré avec login, pwd, clé publique Pailler + la liste des votants
#question : est ce qu'on chiffre la clé publique pailler ? non je pense

def createListReturn() :
    token = BverifLoginPwd.returnToken()
    publick_paillier = EverifLogin.returnPublicKeyPaillier()
    dictCandidats = ClisteCandidats.getCandidates()
    res=[token, publick_paillier, dictCandidats]
    return res

def sendtoVoter() :
    return createListReturn()
