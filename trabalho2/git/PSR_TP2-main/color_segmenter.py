#!/usr/bin/env python
import json
import cv2

import numpy as np


def nothing(x):
    pass


def main():
    # initial setup
    window_name = "Color Segmenter"
    capture = cv2.VideoCapture(0)
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    # create trackbars for color change
    cv2.createTrackbar("B_minimo", window_name, 0, 255, nothing)
    cv2.createTrackbar("R_minimo", window_name, 0, 255, nothing)
    cv2.createTrackbar("G_minimo", window_name, 0, 255, nothing)
    
  
    cv2.createTrackbar("B_maximo", window_name, 0, 255, nothing) 
    cv2.createTrackbar("R_maximo", window_name, 0, 255, nothing)
    cv2.createTrackbar("G_maximo", window_name, 0, 255, nothing)

    while True:
        _, image = capture.read()  # get an image from the camera

        # get current positions of trackbars
        b_min = cv2.getTrackbarPos("B_minimo", window_name)
        b_max = cv2.getTrackbarPos("B_maximo", window_name)

        g_min = cv2.getTrackbarPos("G_minimo", window_name)
        g_max = cv2.getTrackbarPos("G_maximo", window_name)

        r_min = cv2.getTrackbarPos("R_minimo", window_name)
        r_max = cv2.getTrackbarPos("R_maximo", window_name)

        # create a mask for the image according to the trackbars
        lower_bound = np.array([b_min, g_min, r_min])
        upper_bound = np.array([b_max, g_max, r_max])
        thresholded_img = cv2.inRange(image, lower_bound, upper_bound)

        # Visualization of the mask and the trackbars applied to the image
        cv2.imshow(window_name, thresholded_img)
        pressed_key = cv2.waitKey(30)

        # save the values of the trackbars
        if pressed_key == -1:
            pass
        elif chr(pressed_key) == "q":  # Quite the program
            exit(0)
        elif chr(pressed_key) == "w":  # Clear the drawing
            file_name = "limits.json"
            with open(file_name, "w") as file_handle:
                print("writing dictionary d to file " + file_name)
                limits = {
                    "limits": {
                        "B": {"max": b_max, "min": b_min},
                        "G": {"max": g_max, "min": g_min},
                        "R": {"max": r_max, "min": r_min},
                    }
                }
                json.dump(limits, file_handle)  # d is the dicionary


if __name__ == "__main__":
    main()
