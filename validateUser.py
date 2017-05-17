from PasswordBase.base_reader import read_password_base
from PasswordConvertion.convertion import encrypt_to_sha256, encrypt_to_sha1, encrypt_to_md5

base_file_path = './PasswordBase/base.txt'
base_md5_file_path = './PasswordBase/base_md5.txt'
base_sha1_file_path = './PasswordBase/base_sha1.txt'
base_sha256_file_path = './PasswordBase/base_sha256.txt'


def validate_user_md5(username, password):
    digest = encrypt_to_md5(password)
    return validate_user(username, digest, base_md5_file_path)


def validate_user_sha1(username, password):
    digest = encrypt_to_sha1(password)
    return validate_user(username, digest, base_sha1_file_path)


def validate_user_sha256(username, password):
    digest = encrypt_to_sha256(password)
    return validate_user(username, digest, base_sha256_file_path)


def validate_user(username, digest, base_file):
    base = read_password_base(base_file)

    for user in base:
        if user[0] == username and user[1] == digest:
            return True

    return False


print validate_user_md5('Denis.Ozires.Quelip', 'RIUPLKHD')
print validate_user_md5('Rogerio.Bandit.Santos', 'KUKNadNFEJ')