import DcreateToken
import sys
import os

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Verif")

import paillier_generate_key


#récupération clé publique Paillier
def getPublicKeyPaillier() :
  public_key_paillier = paillier_generate_key.get_key_pair().public_key
  return public_key_paillier

