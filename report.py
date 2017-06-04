# coding=utf-8
from PasswordBase.base_reader import decrypt_base_password, read_password_base
from PasswordBase.base_writer import writeNewBase
from PasswordConvertion.convertion import encrypt_to_sha256, encrypt_to_sha1, encrypt_to_md5
import time
import numpy as np
import matplotlib.pyplot as plt

base_file_path = './PasswordBase/'


def count_time(hash_name, converstion_func):
    start_time = time.time()
    base_list = read_password_base(base_file_path + 'base.txt')
    list = decrypt_base_password(base_list)
    convert_list(list, converstion_func, hash_name)
    timeUsed = (time.time() - start_time)
    return timeUsed

times = 50

def convert_list(list, convertion_func, hash_hame):
    for line in list:
        line[1] = convertion_func(line[1])
    writeNewBase(base_file_path + 'base_' + hash_hame + '.txt', list)


def reportMD5():
    md5Times = []
    for x in range(0, times):
        md5Times.append(count_time('md5', encrypt_to_md5))

    report('MD5', md5Times)
    return md5Times


def reportSHA1():
    sha1Times = []
    for x in range(0, times):
        sha1Times.append(count_time('sha1', encrypt_to_sha1))

    report('SHA1', sha1Times)
    return sha1Times


def reportSHA256():
    sha256Times = []
    for x in range(0, times):
        sha256Times.append(count_time('sha256', encrypt_to_sha256))

    report('SHA256', sha256Times)
    return sha256Times


def report(name, array):
    var = np.var(array)

    print("Mean %s --- %s seconds ---" % (name, np.average(array)))
    print("Min %s --- %s seconds ---" % (name, np.amin(array)))
    print("Max %s --- %s seconds ---" % (name, np.amax(array)))
    print("Var %s --- %s seconds ---" % (name, var))
    print("DP %s --- %s seconds ---" % (name, np.sqrt(var)))


def ploting(x1, x2, x3):
    plt.plot(x1, 'r--', label='MD5')
    plt.plot(x2, 'b--', label='SHA1')
    plt.plot(x3, 'g--',  label='SHA256')

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)

    # Save the mapping and save the image
    plt.savefig('time_comparation.png')
    plt.show()


x1 = reportMD5()
x2 = reportSHA1()
x3 = reportSHA256()

ploting(x1, x2, x3)
