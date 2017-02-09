from subprocess import call

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

springParams = ((66,60), (320,240))
showVideo = 0

cameraToBoilerHeight = 10

ser = serial.Serial('/dev/ttyAMA0', baudrate = 115200)

#Read the camera once to make it ready when the first request is sent
ret, frame = video_capture.read()

#set the camera exposure to minimum
call(['./SetExposure.sh'])

while(True):
    data = ser.readline()
    ser.flush()

    print "incoming: "+data
	
    if '0' in data:
        #ret, frame = video_capture.read()
        #sendData = BoilerLine.findBoilerLine(ret, frame)
        sendData = 'BoilerLine not working yet :('
    elif '1' in data:
        ret, frame = video_capture.read()
        x,y = BoilerStack.findBoilerStack(ret, frame)
        xDeg, yDeg = PixelsToDegrees.screenPixelsToDegrees(x,y,(60,66),(320,240))
        if yDeg != 0:
            dist = cameraToBoilerHeight / math.tan(math.radians(yDeg))
        else:
            dist = 0
        sendData = (xDeg, dist)

    elif '2' in data:
        ret, frame = video_capture.read()
        sendData = LineFollower.lineOffset(ret, frame)
    elif '3' in data:
        ret, frame = video_capture.read()
        x,y = SpringDetect.findSpring(ret, frame)
        params = springParams
        sendData = PixelsToDegrees.screenPixelsToDegrees(x,y,(60,66),(320,240))
    else:
        sendData = 'Bad request: ' + data
    ser.write(bytes(sendData))
    print 'sent: \"' + str(sendData) + '\"'
    #Show Window
    if showVideo == 1:
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
