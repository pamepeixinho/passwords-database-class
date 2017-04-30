import csv


def writeNewBase(base_file_path, newList):
    with open(base_file_path, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(w for w in newList)
