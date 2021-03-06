#!/usr/bin/env python
from subprocess import call

import numpy as np
import cv2
import math
import sys
import time
import serial

from VideoInputStream import VideoInputStream
import PixelsToDegrees
import BoilerLine
import BoilerStack
import LineFollower
import SpringDetect

import hash

video_capture = VideoInputStream(source=-1).start()
#video_capture.set(3, 320)
#video_capture.set(4, 240)

showVideo = 1

cameraToBoilerHeight = 2.6
cameraUpAngle = 15

ser = serial.Serial('/dev/ttyAMA0', baudrate = 115200)

def main():
    data = ser.readline()
    ser.flush()
    ret, frame = video_capture.read()
    print "incoming: "+data
	
    if '0' in data:
        #ret, frame = video_capture.read()
        #sendData = BoilerLine.findBoilerLine(ret, frame)
        sendData = 'BoilerLine not working yet :('
    elif '1' in data:
        x,y = BoilerStack.findBoilerStack(ret, frame)
        if (x,y) == (0,0):
		    sendData = "None"
        else:
		    xDeg, yDeg = PixelsToDegrees.screenPixelsToDegrees(x,y,(30,58.6),(640,480))
		    yDeg -=cameraUpAngle
		    if yDeg != 0:
		    	dist = cameraToBoilerHeight / math.tan(math.radians(yDeg))
		    else:
		    	dist = 0
		    sendData = str(-xDeg) + ";" + str(dist)

    elif '2' in data:
        sendData = LineFollower.lineOffset(ret, frame)
    elif '3' in data:
        x,y = SpringDetect.findSpring(ret, frame)
        if x != 0:
            xDeg, yDeg = PixelsToDegrees.screenPixelsToDegrees(x,y,(30,33),(640,480))
            sendData = str(xDeg) + ";" + "0.0"
        else:
            sendData = "None"
    else:
        sendData = 'Bad request: ' + data
	print str(sendData)
	Hash = hash.oneAtATime(sendData)
	
	print Hash
	#sendData = sendData + ";" + str(Hash)
	
    ser.write(bytes(sendData))
    print 'sent: \"' + str(sendData) + '\"'
    
    
    #Show Window
    if showVideo == 1:
        cv2.imshow('frame',frame)

while True:
	try:
		main()
	except(KeyboardInterrupt, SystemExit):
		video_capture.stop()
		sys.exit(0)
