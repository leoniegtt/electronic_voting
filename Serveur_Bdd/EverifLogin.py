import DcreateToken
import sys
import os

sys.path.append(os.path.dirname(__file__) + "/../Serveur_Verif")

import DBToken
import paillier_generate_key

#envoie login chiffré et hashé  pour vérification auprès du système Vérif et récupération clé publique Pailler

#récupération clé publique Paillier
def getPublicKeyPaillier() :
  publick_paillier = paillier_generate_key.generate_key()
  return publick_paillier

publick_paillier = getPublicKeyPaillier()

def returnPublicKeyPaillier() :
  return publick_paillier

#on appelle une fois et on conserve la clé publique dans une variable globale  
publick_paillier = getPublicKeyPaillier()

#envoie login/pwd chiffré et hashé
def sendToken():
  return DcreateToken.tokenCreated()

#renvoie le résultat du vérificateur
#false si le login/pwd a déjà été utilisé
#true sinon
def checkLoginOK() :
   #lien vers le serveur de vérification que les logins n'ont pas déjà été utilisés
  token = sendToken()
  res = DBToken.isTokenExists(token)
  return res
