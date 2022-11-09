#!/usr/bin/env python3
from copy import deepcopy
import datetime
import json
import cv2
import argparse
from matplotlib.pyplot import draw
import numpy as np


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
    rectangles = []

    # Shapes draw variables
    drawing = False
    drawing_rectangle = False
    drawing_circle = False
    draw_initial_coords = None
    whiteboard_before_drawing = None
    last_drawing = ""
    last_circle = None
    last_rectangle = None
    drawing_elipse=False
    last_elipse=None

    # Paint variables
    image_path = "images/paint.png"
    image_checked="images/original.png"
    image_checked=cv2.imread(image_checked)
    capture = cv2.VideoCapture(0)
    clear = True  # clear Memory
    while True:
        _, image = capture.read()
        image = cv2.flip(image, 1)
        # resizing the image, so its all the same
        resized_img = cv2.resize(
            image,
            (int(image.shape[1] * 1), int(image.shape[0] * 1)),
            interpolation=cv2.INTER_AREA,
        )
        #getting the input from limits.json, so we can use it to paint
        lower_bound = np.array([b_min, g_min, r_min])
        upper_bound = np.array([b_max, g_max, r_max])
        thresholded_img = cv2.inRange(resized_img, lower_bound, upper_bound)

        #change of the whiteboard to the input from the camera
        if args["video_canvas"]:
            whiteboard = resized_img

            # Draw previous lines into the new frame
            if clear is True:
                lines = []
                circles = []
                rectangles = []
                last_drawing = ""
                last_circle = None
                last_rectangle = None
                last_elipse=None
                elipses=[]
                clear = False
            else: #drawing the lines, circles ,rectangles and elipses
                for l in lines:
                    cv2.line(
                        whiteboard,
                        (l[0][0], l[0][1]),
                        (l[1][0], l[1][1]),
                        l[2],
                        l[3],
                        cv2.LINE_4,
                    )
                for c in circles:
                    cv2.circle(whiteboard, c[0], c[1], c[2], c[3])
                for r in rectangles:
                    cv2.rectangle(whiteboard, r[0], r[1], r[2], r[3])
                for e in elipses:
                    cv2.ellipse(whiteboard,e[0],e[1],e[2],e[3],e[4],e[5],e[6])
        elif args["paint"]: #painting in the picture inputed above
            if clear is True:  

                image_to_paint = cv2.imread(image_path)
                # whiteboard = cv2.imread(image_path)
                # whiteboard = cv2.resize(
                #     whiteboard,
                #     (int(resized_img.shape[1]), int(resized_img.shape[0])),
                #     interpolation=cv2.INTER_AREA,
                # )
                #creating the whiteboard
                whiteboard = np.zeros(
                    [thresholded_img.shape[0], thresholded_img.shape[1], 3],
                    dtype=np.uint8,
                )
                whiteboard.fill(255)
                #resizing the reference image to paint
                image_checked=cv2.resize(image_checked,
                    (int(resized_img.shape[1]), int(resized_img.shape[0])),
                    interpolation=cv2.INTER_AREA,
                )
               
                clear = False
        else:
            if clear is True:   
                whiteboard = np.zeros(
                    [thresholded_img.shape[0], thresholded_img.shape[1], 3],
                    dtype=np.uint8,
                )
                whiteboard.fill(255)

            # If drawing shapes enabled, store the whiteboard without the shape, and the previous frame of the whiteboard
            if drawing:
                if whiteboard_before_drawing is None:
                    whiteboard_before_drawing = deepcopy(whiteboard)
                previous_whiteboard_frame = deepcopy(whiteboard_before_drawing)
            clear = False

        M = cv2.moments(thresholded_img) #desenho de linhas e objetos
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            if (
                last_x is not None and last_y is not None and not drawing
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

                    else:  # if dist too big, nothing is written when shake mode on
                        print("snake prevention was used")
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
                    
                cv2.circle(resized_img, (cX, cY), 0, (0, 0, 255), 2) #the point in the input image

            if drawing: #checks the variable drawing, if true draws the shape variable thats also true
                if draw_initial_coords is None:
                    draw_initial_coords = (cX, cY)

                if drawing_circle:
                    last_drawing = "circle"

                    radius = int(((cX - draw_initial_coords[0]) ** 2 + (cY - draw_initial_coords[1]) ** 2) ** (1 / 2))
                    if args["video_canvas"]:
                        cv2.circle(whiteboard, draw_initial_coords, radius, color, thickness)
                        last_circle = [draw_initial_coords, radius, color, thickness]
                    else:
                        cv2.circle(previous_whiteboard_frame, draw_initial_coords, radius, color, thickness)

                elif drawing_rectangle:
                    last_drawing = "rectangle"

                    if args["video_canvas"]:
                        cv2.rectangle(whiteboard, draw_initial_coords, (cX, cY), color, thickness)
                        last_rectangle = [draw_initial_coords, (cX, cY), color, thickness]
                    else:
                        cv2.rectangle(previous_whiteboard_frame, draw_initial_coords, (cX, cY), color, thickness)
                
                elif drawing_elipse:
                    last_drawing= "elipse"
                    if args["video_canvas"]:
                        cv2.ellipse(whiteboard,draw_initial_coords,(cX,cY),0,0,0,color,thickness)
                        last_elipse=[draw_initial_coords,(cX,cY),0,0,360,color,thickness]
                    else:
                        cv2.ellipse(previous_whiteboard_frame,draw_initial_coords,(cX,cY),0,0,360,color,thickness)

            else: # use for drawing the final shape and inputting it to the whiteboard
                if draw_initial_coords is not None:
                    # When the draw process stops, draw the definitive shape in the frame

                    if last_drawing == "circle":
                        radius = int(((cX - draw_initial_coords[0]) ** 2 + (cY - draw_initial_coords[1]) ** 2) ** (1 / 2))
                        cv2.circle(whiteboard, draw_initial_coords, radius, color, thickness)
                        draw_initial_coords = None
                        whiteboard_before_drawing = None
                    elif last_drawing == "rectangle":
                        cv2.rectangle(whiteboard, draw_initial_coords, (cX, cY), color, thickness)
                        draw_initial_coords = None
                        whiteboard_before_drawing = None

                    elif last_drawing == "elipse":
                        cv2.ellipse(whiteboard,draw_initial_coords,(cX,cY),0,0,360,color,thickness)
                        draw_initial_coords = None
                        whiteboard_before_drawing = None

                # In case the video frame is the board, store all the shapes to draw every new frame
                if last_circle is not None:
                    circles.append(last_circle)
                    last_circle = None
                elif last_rectangle is not None:
                    rectangles.append(last_rectangle)
                    last_rectangle = None
                elif last_elipse is not None:
                    elipses.append(last_elipse)
                    last_elipse = None

            # Last centroid coords
            last_x = cX
            last_y = cY

        else: #se não encontrar objetos 
                print("no object found")

        cv2.imshow("captured video", resized_img)
        cv2.imshow("video", thresholded_img)

        if args["video_canvas"]:
            cv2.imshow("whiteboard", whiteboard)
        else:
            if drawing:
                cv2.imshow("whiteboard", previous_whiteboard_frame)
            else:
                cv2.imshow("whiteboard", whiteboard)



        pressed_key = cv2.waitKey(100)
        pressed_key = chr(pressed_key & 0xFF)
        print( pressed_key)
        match pressed_key: #the possible inputs for the user to use
            case "q":  # Quit the program
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
                drawing = True
                drawing_circle = True
            case "s":  # draw rectangle
                print("drawing rectangle")
                drawing = True
                drawing_rectangle = True
            case "e": # draw elipse (moving the phone horizontally makes the elipse more horizontal, same for vertical )
                # TODO: add angle to the elipse? 
                print("drawing elipse")
                drawing = True
                drawing_elipse = True
            case "t":
                if args["paint"]:
                   #whiteboard  is the painted image, image_checked is the painted image.
                    #subtract the painted image from the whiteboard to get the image without the painted image
                    error=cv2.subtract(image_checked,whiteboard)
                    
                    average_error=cv2.mean(error)[0]
                    print(average_error)
                    print("the average value of acuracy is: "+str((average_error)/  255 *100) +" %")
           
                
            case other:
                print("no key")
                drawing = False
                drawing_circle = False
                drawing_rectangle = False
                drawing_elipse= False

def main():

    #argparse for the user input and variables for it 
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Definition of test mode")
    parser.add_argument("-j", "--json", required=True, help="Full path to json file.")
    parser.add_argument(
        "-v",
        "--video-canvas",
        required=False,
        help="Use video streaming as canvas",
        action="store_true",
    )
    parser.add_argument("-p",
        "--paint",
        required=False,
        help="Use a numerical canvas to paint. colors to use       1:blue\n  2:red \n  3:green \n  press 't' to check the acuracy",
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

    args = vars(parser.parse_args())

    try:
        with open(args["json"]) as f:
            limits = json.load(f)

            painting(args, limits)
    except FileNotFoundError:
        print("Ficheiro não encontrado.")


if __name__ == "__main__":
    main()
