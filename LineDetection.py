import cv2
import numpy as np


cap = cv2.VideoCapture(0)

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


    cv2.imshow('Perspective Transform', median)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
