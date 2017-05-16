import PasswordBase.base_reader as base_reader
import PasswordBase.base_writer as base_writer
import PasswordConvertion.convertion as convertion
import time
import numpy as np

base_file_path = './PasswordBase/'


def countTime(hashName, converstionFunc):
    start_time = time.time()
    base_list = base_reader.read_password_base(base_file_path + 'base.txt')
    list = base_reader.decrypt_base_password(base_list)
    convert_list(list, converstionFunc, hashName)
    timeUsed = (time.time() - start_time)
    # print("TIMEUSED %s --- %s seconds ---" % (hashName, timeUsed))
    return timeUsed


def convert_list(list, convertionFunc, hashName):
    for line in list:
        line[1] = convertionFunc(line[1])
    base_writer.writeNewBase(base_file_path + 'base_' + hashName + '.txt', list)


def reportMD5():
    md5Times = []
    for x in range(0, 10):
        md5Times.append(countTime('md5', convertion.encrypt_to_md5))

    report('MD5', md5Times)
    # print md5Times
    # mean = np.average(md5Times)
    # print("Mean %s --- %s seconds ---" % ('md5', mean))


def reportSHA1():
    sha1Times = []
    for x in range(0, 10):
        sha1Times.append(countTime('sha1', convertion.encrypt_to_sha1))

    report('SHA1', sha1Times)
    # print md5Times
    # mean = np.average(sha1Times)
    # print mean
    # print("Mean %s --- %s seconds ---" % ('sha1', mean))


def reportSHA256():
    sha256Times = []
    for x in range(0, 10):
        sha256Times.append(countTime('sha256', convertion.encrypt_to_sha256))

    report('SHA256', sha256Times)


def report(name, array):
    mean = np.average(array)
    min = np.amin(array)
    max = np.amax(array)
    var = np.var(array)
    dp = np.sqrt(var)

    print("Mean %s --- %s seconds ---" % (name, mean))
    print("Min %s --- %s seconds ---" % (name, min))
    print("Max %s --- %s seconds ---" % (name, max))
    print("Var %s --- %s seconds ---" % (name, var))
    print("DP %s --- %s seconds ---" % (name, dp))


reportMD5()
reportSHA1()
reportSHA256()
