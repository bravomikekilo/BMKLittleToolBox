#! /usr/bin/env python3

import numpy as np
import argparse

def fromNCHWtoNHWC(X):
    assert X.ndim >= 3 and X.ndim <= 4, "bad ndarray shape"
    if X.ndim == 3:
        return X.copy()
    return X.transpose(0, 2, 3, 1)


def fromNHWCtoNCHW(X):
    assert X.ndim >= 3 and X.ndim <= 4, "bad ndarray shape"
    if X.ndim == 3:
        return X.copy()
    return X.transpose(0, 3, 1, 2)

def main():
    parser = argparse.ArgumentParser(description="switch format between NCHW to NHWC")
    parser.add_argument("npy", type=str)
    parser.add_argument("dest", type=str)
    parser.add_argument('--to', type=str)
    parser.add_argument('--from', type=str)
    args = parser.parse_args()
    pass


if __name__ == '__main__':
    main()



