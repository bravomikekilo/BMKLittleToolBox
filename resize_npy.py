#! /usr/bin/env python3

import numpy as np
from channel_switch import fromNCHWtoNHWC, fromNHWCtoNCHW
from skimage import transform
import argparse

parser = argparse.ArgumentParser(description="resize a batch of image")
parser.add_argument('npy', type=str, help='path of input npy file')
parser.add_argument('dest', type=str, help='path of output npy file')
parser.add_argument('height', type=int, help='resized height')
parser.add_argument('width', type=int, help='resized width')


args = parser.parse_args()

array = np.load(args.npy)
ret = []
shape = (args.height, args.width)
if array.ndim == 3:
    for i, x in enumerate(array):
        ret.append(transform.resize(x, shape))

if array.ndim == 4:
    ret = fromNCHWtoNHWC(ret)
    array = fromNCHWtoNHWC(array)
    for i, x in enumerate(array):
        ret.append(transform.resize(x, shape))
    ret = fromNHWCtoNCHW(ret)

resized = np.array(ret)
dest_name = args.dest
resized.dump(dest_name)






