from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os
import Serveur_Verif.verify_token as vf
tokens = []
def generate_token(login, private_key):
    random_value = os.urandom(16)
    message = login.encode() + random_value
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    login_len = len(login)
    token = bytes([login_len]) + login.encode() + random_value + signature
    return token.hex()

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

token1 = generate_token("login", private_key)
token2 = generate_token("login", private_key)

is_valid1 = vf.verify_token(token1, public_key_pem,"login")
is_valid2 = vf.verify_token(token2, public_key_pem,"login")

if(is_valid1 and is_valid2):
    print("Valid")
    tokens.append(token1)
    tokens.append(token2)
    print("List of tokens:")
    for token in tokens:
        print(token)
else:
    print("Not Valid")
