import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(16)

def generate_iv():
    return get_random_bytes(16)

def ebc_encrypt(file, key):
    ...
def cbc_encrypt(file, key, iv):
    ...

def main():
    key = generate_key()
    iv = generate_iv()
    


if __name__ == '__main__':
    main()