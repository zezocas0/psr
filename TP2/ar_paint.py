#!/usr/bin/env python3
from copy import deepcopy
import datetime
import json
from pickle import NONE
import cv2
import argparse
import numpy as np
from sqlalchemy import false


def painting(args, val):

    # Initialization
    print(args)
    print(val["limits"])
    limits = val["limits"]
    # limite B,G,R
    b = limits["B"]
    g = limits["G"]
    r = limits["R"]

    # min and max values of each color
    b_max = b["max"]
    b_min = b["min"]
    g_max = g["max"]
    g_min = g["min"]
    r_max = r["max"]
    r_min = r["min"]

    last_x = None
    last_y = None

    # Video stream variables
    color = (0, 0, 255)
    thickness = 3
    lines = []
    circles = []
    rectangles=[]

    # Shapes draw variables
    drawing_circle = False
    draw_initial_coords_c = None
    whiteboard_before_drawing_c = None
    last_circle = None

    draw_initial_coords_r = None
    whiteboard_before_drawing_r = None
    drawing_rectangle= False
    last_rectangle = None   
        
     
    capture = cv2.VideoCapture(0)
    clear = True  # clear Memory
    while True:
        _, image = capture.read()
        image = cv2.flip(image, 1)
        resized_img = cv2.resize(
            image,
            (int(image.shape[1] * 0.4), int(image.shape[0] * 0.4)),
            interpolation=cv2.INTER_AREA,
        )
        # variables for the tresholded image
        lower_bound = np.array([b_min, g_min, r_min])
        upper_bound = np.array([b_max, g_max, r_max])
        thresholded_img = cv2.inRange(resized_img, lower_bound, upper_bound)

        if args["video_canvas"]:  #transforms the whiteboard to the input image
            whiteboard = resized_img

            # Draw previous lines into the new frame
            if clear is True: #clearing all objects
                lines = []
                circles = []
                last_circle = None
                rectangles=[]
                last_rectangle = None
                
                clear = False
            else:
                # uses lines variable for the lines
                for l in lines:
                    cv2.line(
                        whiteboard,
                        (l[0][0], l[0][1]),
                        (l[1][0], l[1][1]),
                        l[2],
                        l[3],
                        cv2.LINE_4,
                    )
                #use of circle variable for the circles
                for c in circles:
                    cv2.circle(whiteboard, c[0], c[1], c[2], c[3])
                for r in rectangles:
                    cv2.rectangle(whiteboard, r[0], r[1], r[2], r[3])
        else:
            if clear is True:
                whiteboard = np.zeros(
                    [thresholded_img.shape[0], thresholded_img.shape[1], 3],
                    dtype=np.uint8,
                )
                whiteboard.fill(255)

            # If drawing shapes enabled, store the whiteboard without the shape, and the previous frame of the whiteboard
            if drawing_circle:
                if whiteboard_before_drawing_c is None:
                    whiteboard_before_drawing_c = deepcopy(whiteboard)
                previous_whiteboard_frame = deepcopy(whiteboard_before_drawing_c)
            
            if drawing_rectangle:
                if whiteboard_before_drawing_r is None:
                    whiteboard_before_drawing_r = deepcopy(whiteboard)
                previous_whiteboard_frame = deepcopy(whiteboard_before_drawing_r)

            clear = False

        #finds the mean point of the tresholded image 
        #draws a line or one of the objects(rectangle, circle, elipse)
        M = cv2.moments(thresholded_img)
        if M["m00"] != 0:    
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            if (
                last_x is not None and last_y is not None and not drawing_circle and not drawing_rectangle
            ):  # writes the line on the whiteboard
                if args["use_shake_prevention"]:
                    dist = ((cX - last_x) ** 2 + (cY - last_y) ** 2) ** (1 / 2)
                    if dist < 15:
                        cv2.line(
                            whiteboard,
                            (cX, cY),
                            (last_x, last_y),
                            color,
                            thickness,
                            cv2.LINE_4,
                        )
                        if cX != last_x and cY != last_y:
                            lines.append([(cX, cY), (last_x, last_y), color, thickness])

                    else:  # if the distance is too big, nothing is written
                        pass
                else:
                    cv2.line(
                        whiteboard,
                        (cX, cY),
                        (last_x, last_y),
                        color,
                        thickness,
                        cv2.LINE_4,
                    )

                    if cX != last_x and cY != last_y:
                        lines.append([(cX, cY), (last_x, last_y), color, thickness])
                    
                cv2.circle(resized_img, (cX, cY), 0, (0, 0, 255), 2)  # the point in the input image 


            if drawing_circle:
                if draw_initial_coords_c is None:
                    draw_initial_coords_c = (cX, cY)
                else:
                    radius = int(((cX - draw_initial_coords_c[0]) ** 2 + (cY - draw_initial_coords_c[1]) ** 2) ** (1 / 2))
                    if args["video_canvas"]:
                        cv2.circle(whiteboard, draw_initial_coords_c, radius, color, thickness)
                        last_circle = [draw_initial_coords_c, radius, color, thickness]
                    else:
                        cv2.circle(previous_whiteboard_frame, draw_initial_coords_c, radius, color, thickness)
            else:
                # When the draw process stops, draw the definitive shape in the frame
                if draw_initial_coords_c is not None:
                    radius = int(((cX - draw_initial_coords_c[0]) ** 2 + (cY - draw_initial_coords_c[1]) ** 2) ** (1 / 2))
                    cv2.circle(whiteboard, draw_initial_coords_c, radius, color, thickness)
                    draw_initial_coords_c = None
                    whiteboard_before_drawing_c = None
                # In case the video frame is the board, store all the shapes to draw every new frame
                if last_circle is not None:
                    circles.append(last_circle)
            
            if drawing_rectangle: 
                if draw_initial_coords_r is None:
                    draw_initial_coords_r = (cX, cY)
                else:
                    if args["video_canvas"]:
                        cv2.rectangle(whiteboard, draw_initial_coords_r, (cX, cY), color, thickness)
                        last_rectangle = [draw_initial_coords_r, (cX, cY), color, thickness]
                    else:
                        cv2.rectangle(previous_whiteboard_frame, draw_initial_coords_r, (cX, cY), color, thickness)
            else:
                if draw_initial_coords_r is not None:
                    cv2.rectangle(whiteboard, draw_initial_coords_r (cX, cY), color, thickness)
                    draw_initial_coords_r = None
                    whiteboard_before_drawing_r = None
                if last_rectangle is not None:
                    rectangles.append(last_rectangle)
            
            # Last centroid coords
            last_x = cX
            last_y = cY

        else:
            print("no object detected")

        cv2.imshow("captured video", resized_img)
        cv2.imshow("video", thresholded_img)

        if args["video_canvas"]:
            cv2.imshow("whiteboard", whiteboard)
        else:
            if drawing_circle :
                cv2.imshow("whiteboard", previous_whiteboard_frame)
            else:
                cv2.imshow("whiteboard", whiteboard)
            
            if drawing_rectangle:
                cv2.imshow("whiteboard", previous_whiteboard_frame)
            else:
                cv2.imshow("whiteboard", whiteboard)

        pressed_key = cv2.waitKey(100)
        pressed_key = chr(pressed_key & 0xFF)

        match pressed_key:
            case "q":  # Quite the program
                exit(0)
            case "c":  # Clear the drawing
                clear = True
            case "r":  # Change color to red
                color = (0, 0, 255)  # red color
                print("showing the color red")
            case "g":  # change  color to green
                color = (0, 255, 0)  # green color
                print("showing the color green")
            case "b":  # changing the color to blue
                color = (255, 0, 0)
                print("showing the color blue")
            case "+":
                thickness += 1
            case "-":
                if thickness == 1:  # se for 0 ou -1 , o programa crasha
                    print("cant make the line thinner!")
                else:
                    thickness -= 1
            case "w":  # save the image
                now = datetime.datetime.now()
                image_file = str(
                    "drawing_" + now.strftime("%a_%b_%d_%-I:%M:%-M_%Y") + ".png"
                )
                cv2.imwrite(image_file, whiteboard)
                print("the whiteboard was saved as: " + image_file + " !")
            case "c":  # cleaning the board
                print("cleaning the board")
                whiteboard.fill(255)
            
            case "o":  # draw circle
                print("drawing circle")
                drawing_circle = True
            case "s": #draw a square
                print("drawing square")
                drawing_rectangle=True
            case other:
                print("no key")
                drawing_circle= False
                drawing_rectangle=False

            # TODO: s =square e = elipse 


def main():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Definition of test mode")
    parser.add_argument("-j", "--json", required=True, help="Full path to json file.")
    parser.add_argument(
        "-v",
        "--video-canvas",
        required=False,
        help="Use video streaming as canvas",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-p",
        "--paint-numeric",
        required=False,
        help="Use a numerical canvas to paint",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-s",
        "--use_shake_prevention",
        required=False,
        help="Use shake prevention",
        action="store_true",
        default=False,
    )
    # parser.add_argument("-h",help=" show this help message and exit")         TODO:
    args = vars(parser.parse_args())

    try:
        with open(args["json"]) as f:
            limits = json.load(f)

            painting(args, limits)
    except FileNotFoundError:
        print("Ficheiro não encontrado.")


if __name__ == "__main__":
    main()
