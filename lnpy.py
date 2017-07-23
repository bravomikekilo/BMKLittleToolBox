#! /usr/bin/env python3

import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description="list npy file shape and other attributes")
parser.add_argument("npys", type=str, nargs='*', help='paths to npy file, leave empty will list all npy file in the directory')

args = parser.parse_args()

format_str = """
=========================================
filename: %s
-----------------------------------------
shape: %s
dtype: %s
max: %f
min: %f
mean: %f
var: %f
=========================================
"""

npys = args.npys
if npys == []:
    npys = [i for i in os.listdir('.') if i.endswith('.npy')]
for npy in npys:
    array = np.load(npy)
    shape = array.shape
    dtype = array.dtype
    arr_max = np.max(array)
    arr_min = np.min(array)
    arr_mean = np.average(array)
    arr_var = np.var(array)
    print(format_str % (npy, shape, dtype, arr_max, arr_min, arr_mean, arr_var))



