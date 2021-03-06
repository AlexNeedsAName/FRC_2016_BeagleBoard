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

#set up the camera at the lower resolution of 320x240. The resolution could also be set to 640x480.
video_capture = VideoInputStream(source=-1).start()

#video_capture.set(3, 320)
#video_capture.set(4, 240)
print "initialized camera"
#Constants for height of goal and camera
cameraToBoilerHeight = 2.6
cameraUpAngle = 15

#Change these two values to run different conencted programs
showVideo = 1
data = 1

#Read the camera once to make it ready when the first request is sent
ret, frame = video_capture.read()

#Main loop


def main():
    if data == 0:
        ret, frame = video_capture.read()
        sendData = BoilerLine.findBoilerLine(ret, frame)
    elif data == 1:
        ret, frame = video_capture.read()
        x,y = BoilerStack.findBoilerStack(ret, frame)
        xDeg, yDeg = PixelsToDegrees.screenPixelsToDegrees(x,y,(30,33),(320,240))
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
        sendData = PixelsToDegrees.screenPixelsToDegrees(x,y,(30,33),(320,240))
    else:
        sendData = 'Error'
    print(sendData)
    #ser.write(bytes(sendData))
    #Quit Key
    if showVideo == 1:
        cv2.imshow('frame',frame)

while True:
	try:
		main()
	except KeyboardInterrupt:
		video_capture.stop()
		sys.exit(0)
