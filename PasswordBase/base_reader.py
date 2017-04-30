import csv

# test caesar http://www.dcode.fr/caesar-cipher
ceaser_shift = 12


def read_password_base(base_file_path):
    with open(base_file_path, 'r') as csvfile:
        base_reader = csv.reader(csvfile, delimiter='|')
        return list(base_reader)


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


def decrypt_base_password(password_base):
    print "decrypt"
    for line in password_base:
        print "before %s" % line[1]
        print "after %s" % caesar_decrypt(line[1])
