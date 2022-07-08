#!/bin/env python3

from matplotlib.pyplot import imshow, ion
from skimage import io
import os

import process
import file_handling
import par

ion() # for displaying plots

files = os.listdir(par.folder)
stems = set(['-'.join([i.split('-')[0], i.split('-')[1]]) for i in files])

for n,stem in enumerate(stems):
    seg_file = par.folder/f'{stem}-GFP.jpg'
    fluo_file = par.folder/f'{stem}-mCherry.jpg'

    seg_img = process.mask(file_handling.read_channel(seg_file, 'green'))
    fluo_img = process.mask(file_handling.read_channel(fluo_file, 'red'))

    comp = process.composite(seg_img, fluo_img)
    io.imsave(par.out_folder/f'{stem}.jpg', comp)
