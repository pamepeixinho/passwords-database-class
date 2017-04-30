import hashlib

# https://docs.python.org/2/library/hashlib.html
# can test here: http://www.sha1-online.com/

# test caesar http://www.dcode.fr/caesar-cipher
ceaser_shift = 12


def encrypt_to_md5(password):
    return hashlib.md5(password).hexdigest()


def encrypt_to_sha1(password):
    return hashlib.sha1(password).hexdigest()


def encrypt_to_sha256(password):
    return hashlib.sha256(password).hexdigest()


def caesar(password, shift):
    password = password.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    secret = ""
    for c in password:
        if c in alphabet:
            num = ord(c)
            num += shift
            if num > ord("z"):  # wrap if necessary
                num -= 26
            elif num < ord("a"):
                num += 26
            secret += chr(num)
        else:
            # don't modify any non-letters in the message; just add them as-is
            secret = secret + c
    return secret.upper()


def caesar_decrypt(password):
    return caesar(password, -ceaser_shift)


def caesar_encrypt(password):
    return caesar(password, ceaser_shift)