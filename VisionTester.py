import numpy as np
import cv2
import math
import sys
import time
import socket

import BoilerLine
import BoilerStack

video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 160)
video_capture.set(4, 120)

#Change these two values to run different conencted programs
showVideo = 1
data = 0

while(True):
    if data == 0:
        ret, frame = video_capture.read()
        sendData = BoilerLine.findBoilerLine(ret, frame, showVideo)
    if data == 1:
        ret, frame = video_capture.read()
        sendData = BoilerStack.findBoilerStack(ret, frame, showVideo)

    print sendData

    #Quit Key
    if showVideo == 1:
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
