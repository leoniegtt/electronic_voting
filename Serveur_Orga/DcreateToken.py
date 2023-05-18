#A EXECUTER dans le terminal avant première utilisation :
#pip install pycryptodome
#pip install cryptography

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

import BverifLoginPwd as B

#taille en bits possibles : 1024, 2048, 3072, 2048 recommandé
key = RSA.generate(2048)
pubk_token = PKCS1_OAEP.new(key.publickey())

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

def totalEncryption(login, pwd) :
  token = createToken(login, pwd)
  token = encodeToken(token)
  token = hashToken(token)
  token = encodeToken(token)
  token = encryptToken(token)
  return token
