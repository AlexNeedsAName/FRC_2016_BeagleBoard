import numpy as np
import cv2
import math
import sys
import time
import socket

import BoilerLine
import BoilerStack
import LineFollower
import SpringDetect

video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 160)
video_capture.set(4, 120)

showVideo = 0

UDP_IP = "0.0.0.0"
UDP_PORT = 3641

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while(True):
    data, addr = sock.recvfrom(256)
    #data = data.split(" ")
    print "incoming: "+data

    if data == "0":
        ret, frame = video_capture.read()
        sendData = BoilerLine.findBoilerLine(ret, frame)
    elif data == "1":
        ret, frame = video_capture.read()
        sendData = BoilerStack.findBoilerStack(ret, frame)
    elif data == "2":
        ret, frame = video_capture.read()
        sendData = LineFollower.lineOffset(ret, frame)
    elif data == "3":
        ret, frame = video_capture.read()
        sendData = SpringDetect.findSpring(ret, frame)
    sock.sendto(str(sendData)+" ", ("roboRIO-3641-FRC.local", 3641))

    data = ""
    #Show Window
    if showVideo == 1:
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
