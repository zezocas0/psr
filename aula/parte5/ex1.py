#!/usr/bin/env python3


import cv2
import argparse



def main():

    parser=argparse.ArgumentParser(description="reading and displaying 2 images")
    parser.add_argument("-i1","--image1",type=str, required=False ,default="/home/josesantos/Documents/UA/Psr/aulas/aula5/atlascar.png")
    parser.add_argument("-i2","--image2",type=str, required=False ,default="/home/josesantos/Documents/UA/Psr/aulas/aula5/atlascar2.png") 

    args=vars(parser.parse_args())
    image_rgb1=cv2.imread(args["image1"],cv2.IMREAD_COLOR)
    image_rgb2=cv2.imread(args["image2"],cv2.IMREAD_COLOR)


    flip_flop= True
    while True:
        if flip_flop:
            flip_flop=False
        else:
            flip_flop:True

        if flip_flop:
            cv2.imshow("rgb Image",image_rgb1)
        else:
            cv2.imshow("rgb image2", image_rgb2)

    
    # image = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR) # Load an image


    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding






if __name__ == '__main__':
    main()  
