#!/usr/bin/env python3


import argparse
from attr import NOTHING
import cv2
title_window = "video"
#processamento do video
capture = cv2.VideoCapture(0) 

cv2.namedWindow(title_window)




#adding trackbars to the window
cv2.createTrackbar('R', title_window, 0, 255, nothing )

while (True): 
	ret, video = capture.read() 
	
    

	cv2.imshow(title_window,video) 
	if cv2.waitKey(1)==ord("q"): #quit
		break 



capture.release()
cv2.destroyAllWindows()