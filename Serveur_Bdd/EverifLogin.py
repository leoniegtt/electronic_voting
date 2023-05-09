import DcreateToken

#envoie login chiffré et hashé  pour vérification auprès du système Vérif et récupération clé publique Pailler

#récupération clé publique Paillier
def getPublicKeyPaillier() :
  publick_paillier = exec("../../...")
  return publick_paillier
publick_paillier = getPublicKeyPaillier()

def returnPublicKeyPaillier() :
  return publick_paillier

#on appelle une fois et on conserve la clé publique dans une variable globale  
publick_paillier = getPublicKeyPaillier()

#envoie login/pwd chiffré et hashé
def sendToken(login, pwd):
  return DcreateToken.totalEncryption(login, pwd)

#renvoie le résultat du vérificateur
#false si le login/pwd a déjà été utilisé
#true sinon
def checkLoginOK() :
  result = exec("../..") #lien vers le serveur de vérification que les logins n'ont pas déjà été utilisés
  return result
