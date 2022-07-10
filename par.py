#!/bin/env python3
'''Configuration.'''

from pathlib import Path as path

# Files
folder = path('/mnt/sysbio/PAULSSON LAB/Personal_Folders/Antoine/Old-school LTEE/Competition/22-07-09 Big competition 1')

# Cropping and masking
mask_radius = 700
corner_x = 160 # x position of top-left corner of the plate
corner_y = 550
bby = (corner_y, corner_y + 2*mask_radius) # bounding box y
bbx = (corner_x, corner_x + 2*mask_radius) # bounding box x
