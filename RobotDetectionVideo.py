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
    lower_white = np.array([0,200,0])
    upper_white = np.array([20,255,255])

    # Threshold the HSV image to get only white colors
    Threshold = cv2.inRange(hsv, lower_white, upper_white)

    #Eliminate small peices of a thresholded image
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(Threshold, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Lines', median)
    cv2.imshow('Threshold', opening)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()