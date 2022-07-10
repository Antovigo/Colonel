#!/bin/env python3

from matplotlib.pyplot import imshow, ion
from skimage import io, util
from numpy import shape
import os

import process
import file_handling
import par

ion() # for displaying plots

files = os.listdir(par.folder/'Images')
stems = list(['-'.join([i.split('-')[0], i.split('-')[1]]) for i in files])

for n in range(len(stems)):
    seg_file = par.folder/f'Images/{stems[n]}-GFP.jpg'
    fluo_file = par.folder/f'Images/{stems[n]}-mCherry.jpg'

    seg_img = process.mask(file_handling.read_channel(seg_file, 'green'))
    fluo_img = process.mask(file_handling.read_channel(fluo_file, 'red'))

    # Segment
    bandpassed = process.bandpass(seg_img)
    colonies = process.threshold(bandpassed, 0.9)

    # imshow(process.composite(seg_img, util.img_as_int(colonies)))
    comp = process.composite(seg_img, fluo_img)
    io.imsave(par.folder/f'Composites/{stems[n]}.jpg', comp)

input()
