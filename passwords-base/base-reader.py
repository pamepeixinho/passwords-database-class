import csv
import string

def read_password_base():
    base_file_path = 'base.txt'

    with open(base_file_path, 'r') as csvfile:
        base_reader = csv.reader(csvfile, delimiter='|')
        return list(base_reader)

def ceaser_decrypt(message, shift):
    message = message.lower()

    secret = ""
    for c in message:
        if c in "abcdefghijklmnopqrstuvwxyz":
            num = ord(c)
            num += shift
            if num > ord("z"):  # wrap if necessary
                num -= 26
            elif num < ord("a"):
                num += 26
            secret = secret + chr(num)
        else:
            # don't modify any non-letters in the message; just add them as-is
            secret = secret + c
    return secret


def decrypt_base_password(base):
    print "decrypt"
    for line in base:
        for line in base:
            print "before %s" % line[1]
            print "after %s" % ceaser_decrypt(line[1], -12)


base = read_password_base()
decrypt_base_password(base)
