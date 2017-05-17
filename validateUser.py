from PasswordBase.base_reader import read_password_base
from PasswordConvertion.convertion import encrypt_to_sha256, encrypt_to_sha1, encrypt_to_md5, caesar_encrypt

import time

base_file_path = './PasswordBase/base.txt'
base_md5_file_path = './PasswordBase/base_md5.txt'
base_sha1_file_path = './PasswordBase/base_sha1.txt'
base_sha256_file_path = './PasswordBase/base_sha256.txt'


def validate_user_md5(username, password):
    start_time = time.time()
    digest = encrypt_to_md5(password)
    valid = validate_user(username, digest, base_md5_file_path)
    time_used = (time.time() - start_time)
    print("time_used MD5 --- %s seconds ---" % time_used)
    return valid


def validate_user_sha1(username, password):
    start_time = time.time()
    digest = encrypt_to_sha1(password)
    valid = validate_user(username, digest, base_sha1_file_path)
    time_used = (time.time() - start_time)
    print("time_used SHA1 --- %s seconds ---" % time_used)
    return valid


def validate_user_sha256(username, password):
    start_time = time.time()
    digest = encrypt_to_sha256(password)
    valid = validate_user(username, digest, base_sha256_file_path)
    time_used = (time.time() - start_time)
    print("time_used SHA256 --- %s seconds ---" % time_used)
    return valid


def validate_user_caesar(username, password):
    start_time = time.time()
    digest = caesar_encrypt(password)
    valid = validate_user(username, digest, base_file_path)
    time_used = (time.time() - start_time)
    print("time_used CEASER --- %s seconds ---" % time_used)
    return valid


def validate_user(username, digest, base_file):
    base = read_password_base(base_file)

    for user in base:
        if user[0] == username and user[1] == digest:
            return True

    return False


print validate_user_caesar('Rogerio.Bandit.Santos', 'KUKNANFEJ')
print validate_user_md5('Rogerio.Bandit.Santos', 'KUKNANFEJ')
print validate_user_sha1('Rogerio.Bandit.Santos', 'KUKNANFEJ')
print validate_user_sha256('Rogerio.Bandit.Santos', 'KUKNANFEJ')
