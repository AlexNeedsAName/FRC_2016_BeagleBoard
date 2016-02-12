import cv2
import numpy as np

#Get current frame from camera
cap = cv2.VideoCapture(0)

#Set size of said frame
#cap.set(3, 160)
#cap.set(4, 120)

while True:

    _, frame = cap.read()

    #Perspective Transform (Currently not properly configured but it works)
    rows,cols,ch = frame.shape
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(frame,M,(300,300))

    #Remove Noise and Grain
    median = cv2.medianBlur(dst,5)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    lower_white = np.array([0,0,200])
    upper_white = np.array([180,50,255])

    # Threshold the HSV image to get only white colors
    Threshold = cv2.inRange(hsv, lower_white, upper_white)

    #Eliminate small peices of a thresholded image
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(Threshold, cv2.MORPH_OPEN, kernel)

    edges = cv2.Canny(opening,50,150,apertureSize = 3)

    lines = cv2.HoughLines(edges,1,np.pi/180,75)
    if lines != None:
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

        cv2.line(median,(x1,y1),(x2,y2),(0,0,255),2)
    else:
        print 'none'

    cv2.imshow('Lines', median)
    cv2.imshow('Threshold', Threshold)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()