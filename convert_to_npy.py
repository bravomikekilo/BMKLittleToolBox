#! /usr/bin/env python3
from scipy.misc import imread
import numpy as np
import os
import argparse

parse = argparse.ArgumentParser(description="util module for convert image to npy file")
parse.add_argument('src', type=str, nargs='+', help='source directory contains images')
parse.add_argument('dest', type=str, help='generated npy file name')
args = parse.parse_args()

abs_src = [os.path.abspath(src) for src in args.src]
for i in abs_src:
    if not os.path.exists(i):
        print("source file or directory %s not exist" % (i))
        exit()


shape = None
images = []
for src in abs_src:
    if os.path.isdir(src):
        filenames = os.listdir(src)
        for filename in filenames:
            img = imread(os.path.join(src, filename))
            if not shape:
                shape = img.shape
            else:
                assert shape == img.shape, ("image %s shape not constant" %
                (filename,))
            images.append(img)
    elif os.path.isfile(src):
        img = imread(src)
        if not shape:
            shape = img.shape
        else:
            assert shape == img.shape, ("image %s shape not constant" % (os.path.basename(src)))
        images.append(img)
    else:
        print("unknown type of src %s" % (src,))
        exit()

dest_name = args.dest
array = np.array(images)
array.dump(dest_name) 
