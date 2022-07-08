#!/bin/env python3
'''Read and write files.'''

from skimage import io

def read_channel(filename, channel):
    '''Open a single channel of an RGB image as an image variable.
    Channel can be "red", "green" or "blue".'''

    channel_id = {'red':0, 'green':1, 'blue':2}[channel]
    return io.imread(filename)[:, :, channel_id]


