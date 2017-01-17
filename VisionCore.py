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

showVideo = 1

UDP_IP = "0.0.0.0"
UDP_PORT = 3641

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

#This starts the video feed (so future calls have faster responses)
ret, frame = video_capture.read()

while(true):
    data, addr = sock.recvfrom(256)
    print data
    
    if data == 0:
        ret, frame = video_capture.read()
        sendData = BoilerLine.findBoilerLine(ret, frame)
    if data == 1:
        ret, frame = video_capture.read()
        sendDistance, sendData = BoilerStack.findBoilerStack(ret, frame)

    #Using addr for the IP doesn't work (not sure why) so I'm using this for now
    sock.sendto(str(sendData)+" ", ("roboRIO-3641-FRC.local", 3641))

    #Show Window
    if showVideo == 1:
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
