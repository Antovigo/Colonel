#!/bin/env python3
'''Functions to process an image.'''

from skimage import io, filters, morphology, util, measure, color, feature, segmentation, img_as_float
import matplotlib.pyplot as plt
import numpy as np

import par

def mask(img):
    '''Crop and mask a plate.'''
    # Crop the image
    cropped = img[par.bby[0]:par.bby[1]+1, par.bbx[0]:par.bbx[1]+1] 

    # Mask the plate
    disk = morphology.disk(par.mask_radius)

    masked = cropped * disk + np.mean(cropped[mask!=0])*(1-disk)
    return masked

def normalize(img, ceil = 1):
    '''Normalize an image.'''
    return (img - np.min(img)) / np.max(img) * ceil

def composite(img1, img2):
    '''Make a two-color composite of two channels.'''
    n1 = normalize(img1)
    n2 = normalize(img2)
    return np.dstack((n2, n1, n1))
