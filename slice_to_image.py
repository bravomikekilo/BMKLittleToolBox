#! /usr/bin/env python3

from scipy.misc import imsave
import numpy as np
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description="slice npy file to a directory of image")
parser.add_argument('npy', type=str, help='path to sliced npy file')
parser.add_argument('dir_name', type=str, help='directory to contain images')
parser.add_argument('-f', '--force', action='store_true', help='slice array even the directory is not empty')
parser.add_argument('-c', '--clean', action='store_true', help='clean destination directory')
parser.add_argument('--prefix', type=str, default='', help='prefix of the image file')
parser.add_argument('--format', type=str, default='png', help='format for image')

args = parser.parse_args()

npy = args.npy
dir_name = args.dir_name
force = args.force
clean = args.clean
prefix = args.prefix
pic_format = args.format

array = np.load(npy)

shape = array.shape
if len(shape) > 4:
    print("ndarray shape %s is not acceptable" % (shape,))
    exit()


abs_dir = os.path.abspath(dir_name)
if os.path.isdir(abs_dir):
    if not len(os.listdir(abs_dir)) == 0:
        if not force:
            print("directory %s is not empty" % (abs_dir,))
            exit()
        if clean:
            shutil.rmtree(abs_dir)
            os.mkdir(abs_dir)
else:
    os.mkdir(abs_dir)

if prefix == "":
    prefix = os.path.basename(npy)
for i, pic in enumerate(array):
    pic_name = "%s-%d.%s" % (prefix, i, pic_format)
    if pic.ndim == 3:
        img = pic.tranpose(2, 0, 1)
    else:
        img = pic
    imsave(os.path.join(abs_dir, pic_name), img)

