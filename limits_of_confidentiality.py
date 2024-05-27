import modes_of_operation as MOP
import os
import urllib.parse

def submit(user_input, key, iv):
    prefix = b"userid=456; userdata="
    suffix = b";session-id=31337"
    new_user_input = urllib.parse.quote(user_input)
    new_user_input = new_user_input.encode()
    text = prefix + new_user_input + suffix
    cipher_text = MOP.cbc_encrypt(text, key, iv)
    return cipher_text

def verify(ciphertext, key, iv):
    plain_text = MOP.cbc_decrypt(ciphertext, key, iv)
    if ";admin=true;" in plain_text:
        return True
    return False

def main():
    key = MOP.generate_key()
    iv = MOP.generate_iv()
    user_input = input("Give a string: ")
    ciphertext = submit(user_input, key, iv)
    if verify(ciphertext, key, iv) is True:
        print("verify function returned true")
    else:
        print("verify function returned false")


if __name__ == '__main__':
    main()
