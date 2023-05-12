#a executer dans le terminal avant utilisation :
#pip install pycryptodome
#pip install cryptography

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

import BverifLoginPwd as B






#import voterLogin




#taille en bits possibles : 1024, 2048, 3072, 2048 recommandé
def createTokenKeys() :
  key = RSA.generate(2048)
  return key
  #retourne key et la stocke dans variable globale au programme

key = createTokenKeys()

def createTokenPublicKey(key) :
  pubk_token = PKCS1_OAEP.new(key.publickey())
  return pubk_token
  #retourne la clé publique et la stocke dans variable globale au programme

pubk_token = createTokenPublicKey(key)

def createTokenPrivateKey(key) :
  privk_token = PKCS1_OAEP.new(key)
  return privk_token

#Token : string : "login, pwd"
def createToken(login, pwd) :
  token = login+','+pwd
  return token

#change Token into byte string
def encodeToken(token) :
  token_encoded = token.encode('ASCII')
  return token_encoded

#hash Token
def hashToken(token) :
  token_hashed = SHA256.new(data=token)
  token_hashed = token_hashed.hexdigest()
  return token_hashed

#chiffrer avec la clé publique
def encryptToken(token) :
  token_encrypted = pubk_token.encrypt(token)
  return token_encrypted

def totalEncryption() :
  (login, pwd) = B.getInformation()
  token = createToken(login, pwd)
  token = encodeToken(token)
  token = hashToken(token)
  token = encodeToken(token)
  token = encryptToken(token)
  return token
token = totalEncryption()

def tokenCreated() :
  return token

#TEST
'''
#print(encryptToken())
#print(hashToken(encodeToken(createToken("thomas", "pwd"))))

chiffre1 = encodeToken(hashToken(encodeToken(createToken("thomas", "pwd"))))
chiffre2 = encodeToken(hashToken(encodeToken(createToken("thomas", "pwd"))))

print(chiffre1)
print(chiffre2)
print(chiffre1 == chiffre2)
#print(encryptToken(encodeToken(hashToken(encodeToken(createToken("thomas", "pwd"))))))
'''