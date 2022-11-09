#!/usr/bin/env python3

import fractions
import cv2

import numpy as  np
import sys
import os


haar_file="./haarcascade_frontalface_default.xml"
def main():
    # initial setup
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    
    capturar = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(haar_file)


    if not capturar.isOpened():
        print("não da para abrir a camera")
        exit()


    while True:
        aux, Frame = capturar.read()  # get an image from the camera
        if not aux:
            print("não recebe framerate")
            exit()   
        

        faces = face_cascade.detectMultiScale(Frame, 1.3, 4)
        print(faces)

        for (x,y,w,h) in faces:
            x1= w-30
            y1= h-30
            cv2.rectangle(Frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.rectangle(Frame,(x,y1),(x+w,y+h),(0,255,0),2)
        
        
        
        
        
        
        
        
        cv2.imshow(window_name,Frame)     # add code to show acquired image
    
        if cv2.waitKey(1)== ord("q"):   # add code to wait for a key press

            
            capturar.release()
            break

if __name__ == '__main__':
    main()






