#!/usr/bin/env python3

import cv2
import argparse









def main():

    # ex) 2.1
    
    image_rgb = cv2.imread("atlascar2.png", cv2.IMREAD_COLOR) # Load an image
    treshold_level  =128

    image_gray = cv2.cvtColor(image_rgb,cv2.COLOR_RGB2GRAY)
    _, image_thresholded = cv2.threshold(image_gray,treshold_level , 255, cv2.THRESH_BINARY)
    
    
     
    cv2.imshow('window rgb', image_rgb)
    
    cv2.imshow('window gray', image_gray)  
    #ex2.b
    cv2.imshow("treshold image",image_thresholded)
    cv2.waitKey(0) # wait for a key press before proceeding




# def main():


#     parser = argparse.ArgumentParser(description='Process some integers.')
#     parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                         help='an integer for the accumulator')
#     parser.add_argument('--sum', dest='accumulate', action='store_const',
#                         const=sum, default=max,
#                         help='sum the integers (default: find the max)')

#     args = parser.parse_args()
#     print (args.accumulate(args.integers))






if __name__ == '__main__':
    main()  
