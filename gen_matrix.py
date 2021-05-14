import numpy as np
import argparse
import os
import pdb

parser = argparse.ArgumentParser()
parser.add_argument("data_dir")
parser.add_argument("loci_list")
parser.add_argument("data_output")

args = parser.parse_args()

def parse_list(filename):
    l = []
    f = open(filename, 'r')
    for line in f.readlines():
        l.append(line.strip())

    return sorted(l)


def parse_dir(dirname):
    dirs = os.listdir(dirname)
    full_dir = []
    for item in dirs:
        if item[0] == '.':
            continue
        full_dir.append(os.path.join(dirname, item))

    return full_dir


loci_list = parse_list(args.loci_list)
dir_list = parse_dir(args.data_dir)

data_matrix = np.zeros((len(dir_list)+1, len(loci_list)+1), dtype='U255')

for file_no, f_name in enumerate(dir_list):
    #print(f"{file_no} out of {len(dir_list)}")
    f = open(f_name, 'r')
    _, name = os.path.split(f_name)
    data_matrix[file_no+1, 0] = name
    for line in f.readlines():
        line = line.split()
        if line[0] in loci_list:
            data_matrix[file_no+1, loci_list.index(line[0])+1] = str(line[1])
    f.close()
    '''
    np_file = np.loadtxt(f, skiprows=1, dtype="U25")
    for i, v in enumerate(np_file):
        if v[0] in loci_list:
            data_matrix[file_no+1, loci_list.index(v[0])+1] = str(v[1])
    '''

data_matrix[0,0] = "file_name"
data_matrix[0,1:] = loci_list
np.savetxt(args.data_output, data_matrix, delimiter=",", fmt="%s")
