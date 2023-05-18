import EgetPublicKeyPaillier
import BverifLoginPwd
import ClisteCandidats


#envoie token chiffré avec login, pwd, la liste des candidats
def createListReturn() :
    token = BverifLoginPwd.returnToken()
    dictCandidats = ClisteCandidats.getCandidates()
    public_key_paillier = EgetPublicKeyPaillier.getPublicKeyPaillier()
    (candidates, candidates_num) = ClisteCandidats.transformCandidates(dictCandidats)
    res=[token, public_key_paillier, candidates, candidates_num]
    return res

def sendtoVoter() :
    return createListReturn()
