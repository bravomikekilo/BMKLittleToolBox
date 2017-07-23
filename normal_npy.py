#! /usr/bin/env python3

import numpy as np
import argparse
from skimage import exposure
from channel_switch import fromNCHWtoNHWC, fromNHWCtoNCHW

parser = argparse.ArgumentParser(description="do normalization on npy")
parser.add_argument('npys', type=str, nargs='+', help='names of npy files which need to be normalized')
parser.add_argument('--method', type=str, default='x1', help='method used for normalization {x1, v1, hist}')
parser.add_argument('--nbins', type=int, default=256, help='num of bins for hist normal, ignored in other method')

args = parser.parse_args()

npys = args.npys
method = args.method
arg_nbins = args.nbins

process = None
if method == 'x1':
    process = x1_normalize
elif method == 'v1':
    process = v1_normalize
elif method == 'hist':
    process = lambda x : hist_normalize(x, arg_nbins)

assert process != None, ("can't find normalization method for option %s" % (method,))

for npy in npys:
    array = np.load(npy)
    ret = process(array)
    ret.dump(npy)
    

def x1_normalize(X):
    mean = np.average(X)
    ma = max(np.max(X) - mean, mean - np.min(X))
    return (X - mean) / ma

def v1_normalize(X):
    mean = np.average(X)
    var = np.var(X)
    return (X - mean) / np.sqrt(var)

def hist_normalize(X, nbins):
    shape = X.shape
    if X.ndim == 2:
        return exposure.equalize_hist(X, nbins=nbins)
    if X.ndim == 3:
        ret = []
        for x in X:
            ret.append(exposure.equalize_hist(x, nbins=nbins))
        return np.array(ret)
    if shape[1] == 1:
        X.resize(shape[0], shape[2], shape[3])        
        ret = hist_normalize(X, nbins=nbins)
        ret.resize(shape[0], 1, shape[2], shape[3])
        return ret

    NHWC = fromNCHWtoNHWC(X)
    ret = []
    for x in NHWC:
        ret.append(exposure.equalize_hist(x))
    return fromNHWCtoNCHW(np.array(ret))
