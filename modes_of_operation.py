import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad_fun(data, block_size=16):
    len_padding = block_size - (len(data) % block_size)
    return data + bytes([len_padding] * len_padding)

def read_file(f):
    with open(f, "rb") as fil:
        header = fil.read(54)
        data = fil.read()
    return header, data

def write_file(f, header, data):
    with open(f, "wb") as fil:
        fil.write(header)
        fil.write(data)

def generate_key():
    return get_random_bytes(16)

def generate_iv():
    return get_random_bytes(16)

def ecb_encrypt(f, key):
    cipher = AES.new(key,AES.MODE_ECB)
    cipher_text = b""
    header, data = read_file(f)
    data = pad_fun(data)
    for i in range(0, len(data), 16):
        one_block = data[i:i+16]
        cipher_text += cipher.encrypt(one_block)
    return header, cipher_text
    
def cbc_encrypt(file, key, iv):
    ...

def main():
    key = generate_key()
    iv = generate_iv()
    header, ecb_cipher = ecb_encrypt("mustang.bmp", key)
    write_file("ecb_mustang_encrypted.bmp", header, ecb_cipher)


if __name__ == '__main__':
    main()