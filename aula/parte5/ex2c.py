#!/usr/bin/env python3

import cv2
import argparse

from matplotlib import image









def main():

    # ex) 2.1
    
    image_rgb = cv2.imread("atlascar2.png", cv2.IMREAD_COLOR) # Load an image
    treshold_level_b  =50
    treshold_level_g =100
    treshold_level_r =150


    
    image_b,image_g,image_r=cv2.split(image_rgb)
    _, image_thresholded_b = cv2.threshold(image_b,treshold_level_b , 255, cv2.THRESH_BINARY)
    _, image_thresholded_g = cv2.threshold(image_g,treshold_level_g , 255, cv2.THRESH_BINARY)
    _, image_thresholded_r = cv2.threshold(image_r,treshold_level_r , 255, cv2.THRESH_BINARY)

    new_rgb_image=cv2.merge((image_thresholded_b,image_thresholded_g,image_thresholded_r))
    
    
     
    cv2.imshow('window rgb', image_rgb)
    
    cv2.imshow('window gray', new_rgb_image)  

    cv2.waitKey(0) # wait for a key press before proceeding

    






if __name__ == '__main__':
    main()  
