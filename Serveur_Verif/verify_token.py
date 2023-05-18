from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import os
import token_list as tl

#entre serveur verif et comptage
#serveur comptage envoie token 2, il veut savoir si oui ou non il est déjà dans la bdd et si il a déjà été utilisé


def verify_token(token, public_key_pem, login):
    public_key = serialization.load_pem_public_key(
        public_key_pem,
        backend=default_backend()
    )
    token_bytes = bytes.fromhex(token)
    login_len = token_bytes[0]
    login_bytes = token_bytes[1:login_len+1]
    random_value = token_bytes[login_len+1:login_len+17]
    signature = token_bytes[login_len+17:]
    message = login_bytes + random_value
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False
