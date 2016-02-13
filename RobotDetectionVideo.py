import cv2
import numpy as np

#Get current frame from camera
cap = cv2.VideoCapture(1)

#Set size of said frame
cap.set(3, 160)
cap.set(4, 120)

while True:

    _, frame = cap.read()

    #Remove Noise and Grain
    median = cv2.medianBlur(frame,5)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    lower_white = np.array([0,150,0])
    upper_white = np.array([40,255,255])

    # Threshold the HSV image to get only white colors
    Threshold = cv2.inRange(hsv, lower_white, upper_white)

    #Eliminate small peices of a thresholded image
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(Threshold, cv2.MORPH_OPEN, kernel)

    #Detect contours in an image
    contours, hierarchy = cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)



    cv2.imshow('Frame',frame)
    cv2.imshow('Threshold', Threshold)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()