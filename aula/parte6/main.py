#!/usr/bin/env python3


from copy import deepcopy
from functools import partial

from colorama import Style, Fore
import cv2
import sys

def mouseCallback(event,x,y,flags,userdata):


    # print ("Mouse event at X= " +str(x) +"  y=  " +str(y))

    if event== cv2.EVENT_LBUTTONDOWN:
        if options["is_drawing"]:
            print ("stop drawing")
            options["is_drawing"]=False
        else:
            print("start drawing")
            options["is_drawing"]=True
    
    elif event== cv2.EVENT_MOUSEMOVE:
        if options["is_drawing"]:
            options["xs"].append(x)
            options["ys"].append(y)    
            

            if len(options["xs"])>2:

                    x1=options["xs"][-2]
                    y1=options["ys"][-2]
                    x2=xoptions["xs"][-1]       
                    y2=options["ys"][-1]
                    cv2.line(options["gui_image"],(x1,y1),(x2,y2), options["pencil_color"], 1)




def main():
 
    image = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR) # Load an image
    
    window_name="window"
    
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name,600,600)




    options={'gui_image':deepcopy(image),'is_drawing':False,'xs':[],'ys':[],'pencil_color':(0,255,0)}


    cv2.setMouseCallback(window_name,partial(mouseCallback,options=options))


    while True:
        cv2.imshow(window_name,options['gui_image'])
        pressed_key=cv2.waitKey(0) # wait for a key press before proceeding
        # print ("pressed key= "+ str(pressed_key))

        if pressed_key ==-1:
            pass
        elif chr(pressed_key)=="q":
            exit(0)
        elif chr(pressed_key)=="c":
            print(Fore.RED+ "you pressed c"+Style.RESET_ALL )
            options['xs']=[]
            options['ys']=[]
            options['gui_image']=deepcopy(image)
        elif chr(pressed_key)=="r":
            options["pencil_color"]=(0,0,255)





if __name__ == '__main__':
    main()  
