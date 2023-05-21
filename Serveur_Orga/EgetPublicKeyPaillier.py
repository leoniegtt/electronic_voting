import DcreateToken
import sys
import os

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Verif")
import paillier_generate_key
import replaceToken

def sendToken1(l_token1) :
  replaceToken.getToken1(l_token1)

#récupération clé publique Paillier
def getPublicKeyPaillier() :
  public_key_paillier = paillier_generate_key.getPublic()
  return public_key_paillier
