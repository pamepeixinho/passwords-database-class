import csv
from PasswordConvertion.convertion import caesar_decrypt


def read_password_base(base_file_path):
    with open(base_file_path, 'r') as csvfile:
        base_reader = csv.reader(csvfile, delimiter='|')
        return list(base_reader)


def decrypt_base_password(password_base):
    password_base = password_base
    for line in password_base:
        line[1] = caesar_decrypt(line[1])
    return password_base
