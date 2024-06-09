import modes_of_operation as MOP
import os
import urllib.parse
import random

def submit(user_input, key, iv):
    prefix = b"userid=456; userdata="
    print(len(prefix))
    suffix = b";session-id=31337"
    new_user_input = urllib.parse.quote(user_input)
    new_user_input = new_user_input.encode()
    text = prefix + new_user_input + suffix
    print(f"Encrypting: {text}")
    cipher_text = MOP.cbc_encrypt(text, key, iv)
    return cipher_text

def verify(ciphertext, key, iv):
    plain_text = MOP.cbc_decrypt(ciphertext, key, iv)
    print(f"Decrypted: {plain_text}")
    if b";admin=true;" in plain_text:
        return True
    return False

def flip_bit(ciphertext):
    modify_cipher = bytearray(ciphertext)
    byte_pos = [33, 39, 44]
    for x in byte_pos:
        block = x // 16
        index = x % 16
        prev = (block - 1) * 16 + index
        if index == 1:
            modify_cipher[prev] ^= (ord("X") ^ ord (";"))
        elif index == 7:
            modify_cipher[prev] ^= (ord("Y") ^ ord ("="))
        elif index == 12:
            modify_cipher[prev] ^= (ord("X") ^ ord (";"))
    return bytes(modify_cipher)

def main():
    key = MOP.generate_key()
    iv = MOP.generate_iv()
    user_input = "AAAAAAAAAAAAXadminYtrueX"
    ciphertext= submit(user_input, key, iv)
    if verify(ciphertext, key, iv) is True:
        print("verify function returned true")
    else:
        print("verify function returned false")

    flipped = flip_bit(ciphertext)
    # print(flipped)
    if verify(flipped, key, iv) is True:
        print("verify with flip bit function returned true")
    else:
        print("verify with flip bit function returned false")

if __name__ == '__main__':
    main()
