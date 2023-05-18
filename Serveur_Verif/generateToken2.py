from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

#taille en bits possibles : 1024, 2048, 3072, 2048 recommandé
key = RSA.generate(2048)
pubk_token = PKCS1_OAEP.new(key.publickey())

def createTokenPrivateKey(key) :
  privk_token = PKCS1_OAEP.new(key)
  return privk_token

#Token : string : "login, pwd"
def createToken(token1) :
  token = str(token1[:50])
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

def totalEncryption(token1) :
  token = createToken(token1)
  token = encodeToken(token)
  token = hashToken(token)
  token = encodeToken(token)
  token = encryptToken(token)
  return token
