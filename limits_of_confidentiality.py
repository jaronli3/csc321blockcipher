import modes_of_operation as MOP
import os
import urllib.parse
import random

def submit(user_input, key, iv):
    prefix = b"userid=456; userdata="
    suffix = b";session-id=31337"
    new_user_input = urllib.parse.quote(user_input)
    new_user_input = new_user_input.encode()
    text = prefix + new_user_input + suffix
    cipher_text = MOP.cbc_encrypt(text, key, iv)
    return cipher_text, len(MOP.pad_fun(text)) // 16

def verify(ciphertext, key, iv):
    plain_text = MOP.cbc_decrypt(ciphertext, key, iv)
    print(plain_text)
    if b";admin=true;" in plain_text:
        return True
    return False

def flip_bit(ciphertext, num_blocks, block_size=16):
    modify_cipher = bytearray(ciphertext)
    admin_true_text = b";admin=true;"
    start = random.randint(1, num_blocks - 1) * block_size
    prev = ciphertext[start - block_size: start]
    xor = MOP.xor_func(admin_true_text, prev)
    for i in range(len(admin_true_text)):
        modify_cipher[start+i] ^= xor[i]

    return bytes(modify_cipher)

def main():
    key = MOP.generate_key()
    iv = MOP.generate_iv()
    user_input = input("Give a string: ")
    ciphertext, num_blocks = submit(user_input, key, iv)
    if verify(ciphertext, key, iv) is True:
        print("verify function returned true")
    else:
        print("verify function returned false")

    flipped = flip_bit(ciphertext, num_blocks)

    if verify(flipped, key, iv) is True:
        print("verify with flip bit function returned true")
    else:
        print("verify with flip bit function returned false")

if __name__ == '__main__':
    main()
