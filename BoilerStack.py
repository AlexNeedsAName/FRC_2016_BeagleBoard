import numpy as np
import cv2
import math
import sys
import time


lower = (36,152,50)
upper = (113,255,255)
minArea = 20
maxArea = 10000
rectangularity = 100
maxLateralDisparity = 25

'''def distance_to_camera(knownWidth, focalLength, perWidth):
    #compute and return the distance from the boiler stack to the camera
    return (knownWidth * focalLength) / perWidth
'''

def findContourPosition(contour):#find the center of the rectangle
    x, y, w, h = cv2.boundingRect(contour)
    x += w / 2
    y += h / 2
    return x,y

def filterContours(contours):
    filteredContours = []
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        area = cv2.contourArea(hull)
        _,_,w,h = cv2.boundingRect(hull)
        rectArea = w*h
        if area > minArea and area < maxArea and (rectArea - area) * 100 / rectArea < rectangularity:  #check if the area is correct and the region is rectangular enoug
            filteredContours.append(hull)
    return filteredContours

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
    if len(contours) != 0:
	    contours = filterContours(contours)
	
    # Find the biggest contour (if detected)
    if len(contours) == 2:
        top = max(contours, key=cv2.contourArea)
        bottom = min(contours, key=cv2.contourArea)
        x1, y1 = findContourPosition(top)
        x2, y2 = findContourPosition(bottom)
        
        '''if cx >= 80:
            direction = cx - 80
        if cx < 80:
            direction = -(80-cx)'''
        #Calculate Distance
        '''if w != 0:
            distance = distance_to_camera(2.25, 204, w)
        else:
            distance = 0'''
        '''font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(distance), (10, 120), font, 1, (255, 0, 0), 2)

        cv2.drawContours(frame, contours, -1, (255,0,0), 1)'''
        
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2
        
        print cx,cy
        return (cx,cy)
    elif len(contours) > 2:
        for i in range(0,len(contours)):#if there's more than 2 contours, find two at the same height.
            for j in range(0,len(contours)):
                if i != j:
                    print i,j
                    x1, y1 = findContourPosition(contours[i])  # find the positions of the contours
                    x2, y2 = findContourPosition(contours[j])
                    if abs(x1 - x2) < maxLateralDisparity:
                        cx = (x1 + x2) / 2
                        cy = (y1 + y2) / 2
                        print cx,cy
                        return (cx,cy)
    return 0,0
    
