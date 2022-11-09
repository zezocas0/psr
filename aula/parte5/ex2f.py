#!/usr/bin/env python3

import cv2
import argparse
from cv2 import merge

import numpy as np








def main():

    # ex) 2.1
    
    image_rgb = cv2.imread("atlas2000_e_atlasmv.png", cv2.IMREAD_COLOR) # Load an image


    lower_bound= np.array([0,0,0])
    upper_bound=np.array([50,255,50])

    image_mask=cv2.inRange(image_rgb,lower_bound,upper_bound)
    image_mask= image_mask.astype(bool)



    b,g,r = cv2.split(image_rgb)
    b[image_mask]=b[image_mask]*1.5
    g[image_mask]=g[image_mask]*1.5
    r[image_mask]=r[image_mask]*1.5
    new_rgb=merge(r,g,b)

    image_mask2=np.logical_not("image_mask")

    cv2.imshow('window rgb', image_rgb)
    
    cv2.imshow('window gray',  new_rgb)  

    cv2.waitKey(0) # wait for a key press before proceeding

    






if __name__ == '__main__':
    main()  
