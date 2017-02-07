
import numpy as np
import cv2
import math
import sys
import time
import serial

import PixelsToDegrees
import BoilerLine
import BoilerStack
import LineFollower
import SpringDetect


video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 320)
video_capture.set(4, 240)

cameraToBoilerHeight = 2.6
cameraUpAngle = 30

#Change these two values to run different conencted programs
showVideo = 1
data = 1

while(True):
    sendData = ''
    if data == 0:
        ret, frame = video_capture.read()
        sendData = BoilerLine.findBoilerLine(ret, frame)
    elif data == 1:
        ret, frame = video_capture.read()
        x,y = BoilerStack.findBoilerStack(ret, frame)
        xDeg, yDeg = PixelsToDegrees.screenPixelsToDegrees(x,y,(60,66),(320,240))
        yDeg -=cameraUpAngle
        if yDeg != 0:
            dist = cameraToBoilerHeight / math.tan(math.radians(yDeg))
        else:
            dist = 0
        sendData = (xDeg, dist)

    elif data == 2:
        ret, frame = video_capture.read()
        sendData = LineFollower.lineOffset(ret, frame)
    elif data == 3:
        ret, frame = video_capture.read()
        sendData = SpringDetect.findSpring(ret, frame)
        x, y = SpringDetect.findSpring(ret, frame)
        sendData = PixelsToDegrees.screenPixelsToDegrees(x,y,(60,66),(320,240))
    print(sendData)
    #ser.write(bytes(sendData))
    #Quit Key
    if showVideo == 1:
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
