#!/usr/bin/env python3

import cv2


import numpy as np








def main():

    # ex) 2.1
    
    image_rgb = cv2.imread("atlas2000_e_atlasmv.png", cv2.IMREAD_UNCHANGED) # Load an image
    treshold_level_b  =50
    treshold_level_g =100
    treshold_level_r =150
    image_hsv= cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)

    lower_bound= np.array([120,10,0])
    upper_bound=np.array([120,100,100])
    image_mask=cv2.inRange(image_hsv,lower_bound,upper_bound)


     
    cv2.imshow('window rgb', image_hsv)
    
    cv2.imshow('window gray', image_mask)  

    cv2.waitKey(0) # wait for a key press before proceeding

    






if __name__ == '__main__':
    main()  
