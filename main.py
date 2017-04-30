import PasswordBase.base_reader as base_reader
import PasswordBase.base_writer as base_writer
import PasswordConvertion.convertion as convertion
import time

base_file_path = './PasswordBase/'


def countTime(hashName, converstionFunc, list):
    start_time = time.time()
    convert_list(list, converstionFunc, hashName)
    print("%s --- %s seconds ---" % (hashName, (time.time() - start_time)))


def convert_list(list, convertionFunc, hashName):
    for line in list:
        line[1] = convertionFunc(line[1])
    base_writer.writeNewBase(base_file_path + 'base_'+hashName+'.txt', list)


base_list = base_reader.read_password_base(base_file_path + 'base.txt')

list = base_reader.decrypt_base_password(base_list)

countTime('md5', convertion.encrypt_to_md5, list)
countTime('sha1', convertion.encrypt_to_sha1, list)
countTime('sha256', convertion.encrypt_to_sha256, list)
