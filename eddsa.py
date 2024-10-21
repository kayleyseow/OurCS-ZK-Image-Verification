from ecdsa import SigningKey 
import json
import base64
# import ed25519
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

# change to eddsa

# convert img to json
photo = {}
with open('cat_img.jpg', mode='rb') as file:
    img = file.read()
photo['img'] = base64.encodebytes(img).decode('utf-8')

sk = Ed25519PrivateKey.generate()

byte_message = json.dumps(photo)
signature = sk.sign(b"byte_message")

pk = sk.public_key()
# Raises InvalidSignature if verification fails
# public_key.verify(signature, b"my authenticated message")

# sk = SigningKey.generate() #secret key
# vk = sk.verifying_key # public key

# # print(byte_message)
# # byte_message = json.dumps(non_string_message).encode('utf-8')
# signature = sk.sign(b'byte_message') #signature
# assert vk.verify(signature, byte_message)

print("secret key: ", sk)
print("public key: ", pk.public_bytes(encoding=serialization.Encoding.Raw,format=serialization.PublicFormat.Raw ))
print("signature: ", signature)
