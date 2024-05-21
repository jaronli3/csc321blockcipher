import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad_fun():
    ...
    
def read_file(f):
    with open(f, "rb") as fil:
        header = f.read(54)
        data = f.read()
    return header, data

def generate_key():
    return get_random_bytes(16)

def generate_iv():
    return get_random_bytes(16)

def ecb_encrypt(file, key):
    cipher = AES.new(key,AES.MODE_ECB)
    cipher_text = b""
    header, data = read_file(file)
    pad_data = pad_fun(data)

def cbc_encrypt(file, key, iv):
    ...

def main():
    key = generate_key()
    iv = generate_iv()
    


if __name__ == '__main__':
    main()