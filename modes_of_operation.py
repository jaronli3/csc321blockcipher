import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad_fun(data, block_size=16):
    len_padding = block_size - (len(data) % block_size)
    return data + bytes([len_padding] * len_padding)

def unpad_fun(data):
    return data[:-data[-1]]

def xor_func(curr, prev):
    answer = bytearray(len(curr))
    for i in range(len(curr)):
        answer[i] = curr[i]^prev[i]
    return bytes(answer)

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

def ecb_encrypt(data, key):
    cipher = AES.new(key,AES.MODE_ECB)
    cipher_text = b""
    data = pad_fun(data)
    for i in range(0, len(data), 16):
        one_block = data[i:i+16]
        cipher_text += cipher.encrypt(one_block)
    return cipher_text

def ecb_decrypt(ciphertext, key):
    cipher = AES.new(key,AES.MODE_ECB)
    plaintext = b""
    for i in range(0, len(ciphertext), 16):
        one_block = ciphertext[i:i+16]
        plaintext += cipher.decrypt(one_block)
    plaintext = unpad_fun(plaintext)
    return plaintext
    
def cbc_encrypt(data, key, iv):
    cipher = AES.new(key,AES.MODE_ECB)
    cipher_text = b""
    prev = iv
    data = pad_fun(data)
    for i in range(0, len(data), 16):
        one_block = data[i:i+16]
        one_block = xor_func(one_block, prev)
        enc_block = cipher.encrypt(one_block)
        cipher_text += enc_block
        prev = enc_block
    return cipher_text

def cbc_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    plain_text = b""
    prev = iv
    for i in range(0, len(ciphertext), 16):
        one_block = ciphertext[i:i+16]
        plain_text_block = xor_func(cipher.decrypt(one_block), prev)
        plain_text += plain_text_block
        prev = one_block
    plain_text = unpad_fun(plain_text)
    return plain_text

def main():
    key = generate_key()
    iv = generate_iv()
    header, data = read_file("mustang.bmp")
    ecb_cipher = ecb_encrypt(data, key)
    write_file("ecb_mustang_encrypted.bmp", header, ecb_cipher)
    if ecb_decrypt(ecb_cipher, key) == data:
        print("Successfully decrypted ecb_mustang")
    cbc_cipher = cbc_encrypt(data, key, iv)
    write_file("cbc_mustang_encrypted.bmp", header, cbc_cipher)
    if cbc_decrypt(cbc_cipher, key, iv) == data:
        print("Successfully decrypted cbc_mustang")


if __name__ == '__main__':
    main()