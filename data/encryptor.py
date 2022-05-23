from cryptography.fernet import Fernet
from os import path

def encrypt(string):

    if path.isfile("data/encryption.key") == False:

        key = Fernet.generate_key()
        keyfile = open("data/encryption.key", 'wb')
        keyfile.write(key)
        keyfile.close()

        fernetInstance = Fernet(key)
        encString = fernetInstance.encrypt(bytes(string, encoding="utf-8"))
        return encString

    else:

        keyfile = open("data/encryption.key", 'rb')
        key = keyfile.read()
        keyfile.close()
        
        fernetInstance = Fernet(key)
        encString = fernetInstance.encrypt(bytes(string, encoding="utf-8"))

        return encString

def decrypt(string):
    keyfile = open("data/encryption.key", 'rb')
    key = keyfile.read()
    keyfile.close()

    fernetInstance = Fernet(key)
    decString = fernetInstance.decrypt(string)

    return decString.decode(encoding="utf-8")