import hashlib


# can test here: http://www.sha1-online.com/

def convert_to_md5(password):
    return hashlib.md5(password).hexdigest()


def convert_to_sha1(password):
    return hashlib.sha1(password).hexdigest()


def convert_to_sha256(password):
    return hashlib.sha256(password).hexdigest()
