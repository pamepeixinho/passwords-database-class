import PasswordBase.base_reader as base_reader
import PasswordBase.base_writer as base_writer
import PasswordConvertion.convertion as convertion
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata

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
    return md5Times


def reportSHA1():
    sha1Times = []
    for x in range(0, 10):
        sha1Times.append(countTime('sha1', convertion.encrypt_to_sha1))

    report('SHA1', sha1Times)
    # print md5Times
    # mean = np.average(sha1Times)
    # print mean
    # print("Mean %s --- %s seconds ---" % ('sha1', mean))
    return sha1Times


def reportSHA256():
    sha256Times = []
    for x in range(0, 10):
        sha256Times.append(countTime('sha256', convertion.encrypt_to_sha256))

    report('SHA256', sha256Times)
    return sha256Times


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


def ploting(x1, x2, x3):
    plt.plot(x1, 'r--',  marker='o', label='MD5')
    plt.plot(x2, 'b--',  marker='o', label='SHA1')
    plt.plot(x3, 'g--',  marker='o', label='SHA256')

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)

    # Save the mapping and save the image
    plt.savefig('time_comparation.png')
    plt.show()


x1 = reportMD5()
x2 = reportSHA1()
x3 = reportSHA256()

ploting(x1, x2, x3)

# http://stackoverflow.com/questions/20412038/printing-python-code-to-pdf OLHAR
