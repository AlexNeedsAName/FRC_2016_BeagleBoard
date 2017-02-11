import numpy as np
import cv2
import math
import sys
import time


lower = (36,152,50)
upper = (113,255,255)


def distance_to_camera(knownWidth, focalLength, perWidth):
    #compute and return the distance from the boiler stack to the camera
    return (knownWidth * focalLength) / perWidth


def findBoilerStack(ret, frame):
    # Gaussian blur
    blur = cv2.GaussianBlur(frame,(5,5),0)

    #Convert to Hue, Saturation, and Value colorspace
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    lower_white = lower
    upper_white = upper

    # Threshold the HSV image to get only white colors
    thresh = cv2.inRange(hsv, lower_white, upper_white)

    # Find the contours of the frame
    _,contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = 0
            cy = 0

        cv2.line(frame,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(frame,(0,cy),(1280,cy),(255,0,0),1)

        if cx >= 80:
            direction = cx - 80
        if cx < 80:
            direction = -(80-cx)

        #Calculate Distance
        if w != 0:
            distance = distance_to_camera(2.25, 204, w)
        else:
            distance = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(distance), (10, 120), font, 1, (255, 0, 0), 2)

        cv2.drawContours(frame, contours, -1, (255,0,0), 1)
        
        x,y,w,h = cv2.boundingRect(c)
        cx = x + w/2
        cy = y + h/2
        print cx,cy
        return (cx,cy)
    else:
        return 0,0
