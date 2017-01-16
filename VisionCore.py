import numpy as np
import cv2
import math
import sys
import time
import socket

video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 160)
video_capture.set(4, 120)

showVideo = true

UDP_IP = ""
UDP_PORT = 3641

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while(true):
    data, addr = sock.recvfrom(256)
    print data
    
    if data == 0:
        sendData = code0
    if data == 1:
        sendData = code1

    sock.sendto(str(sendData)+" ", ("roboRIO-3641-FRC.local", 3641))

    #Quit Key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
