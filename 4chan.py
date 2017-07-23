#! /usr/bin/env python3

import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description='add channel dim to npy')
parser.add_argument('npy', type=str, nargs='+', 'paths to npy files')

args = parser.parse_args()

for npy in args.npy:
    array = np.load(npy)
    if array.ndim != 3: continue
    shape = array.shape
    array.resize(shape[0], 1, shape[1], shape[2])
    array.dump(npy)
