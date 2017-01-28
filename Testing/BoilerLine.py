import numpy as np
import cv2
import math
import sys
import time

lower = (40,96,118)
upper = (79,183,255)

def findBoilerLine(ret, frame):

    # Gaussian blur
    blur = cv2.GaussianBlur(frame,(5,5),0)

    #Convert to Hue, Saturation, and Value colorspace
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = lower
    upper_red = upper

    # Threshold the HSV image to get only white colors
    thresh = cv2.inRange(hsv, lower_red, upper_red)

    # Black and white thresholding
    #ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

    # Find the contours of the frame
    contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)

	#This code is for finding the center of the contour, however I can't figure out how to keep it from returning
	#"Can't divide M['m10'] by zero" even after I added the "if M['m00'] is 0:" loop.
	
	#M = cv2.moments(c)
	#if M['m00'] is 0:
        #    cx = int(M['m10'])
        #    cy = int(M['m01'])
        #else:
	#    cx = int(M['m10']/M['m00'])
        #    cy = int(M['m01']/M['m00'])

	#Draw a crosshair to show the center of the contour
        #cv2.line(frame,(cx,0),(cx,720),(255,0,0),1)
        #cv2.line(frame,(0,cy),(1280,cy),(255,0,0),1)

        # then apply fitline() function
        [vx, vy, x, y] = cv2.fitLine(c, cv2.cv.CV_DIST_L2, 0, 0.01, 0.01)
        # Now find two extreme points on the line to draw line
        lefty = int((-x * vy / vx) + y)
        righty = int(((thresh.shape[1] - x) * vy / vx) + y)

        # Finally draw the line
        cv2.line(frame, (thresh.shape[1] - 1, righty), (0, lefty), 255, 2)

        xDifference = (thresh.shape[1]-1) - 0
        yDifference = righty-lefty

	#I apologize for a lack of a better variable name
        pythagOne = (xDifference*xDifference) + (yDifference*yDifference)
        pythagTwo = math.sqrt(pythagOne)

        #Normalize the vector
        xDifference = (1/pythagTwo)*xDifference
        yDifference = (1/pythagTwo)*yDifference

        lineRadians = math.atan(yDifference/xDifference)

        lineDegrees = math.degrees(lineRadians)

	#Draw the angle of the line on the screen
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(lineDegrees), (10, 120), font, 1, (255, 0, 0), 2)

        cv2.drawContours(frame, contours, -1, (255,0,0), 1)

	#Output the angle of the line to stdout for Client.java to read
        return str(lineDegrees)

    else:
	#If no line is detected say the line's angle is just zero
        return "0"


#Might be useful in future!
#if(__name__ == '__main__'):
#	video_capture = cv2.VideoCapture(-1)
#	video_capture.set(3, 160)
#	video_capture.set(4, 120)
 #       while True:
#		processFrame(video_capture)
#		cv2.imshow('frame',frame)
#		if cv2.waitKey(1) & 0xFF == ord('q'):
#		break
		
