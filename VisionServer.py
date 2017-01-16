#!/usr/bin/env python

import socket
import cv2
import BoilerLine

video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 160)
video_capture.set(4, 120)

UDP_IP = "0.0.0.0"
UDP_PORT = 3641

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while 1:
	request, addr = sock.recvfrom(1024)
	if(request == "RequestBoiler"):
		response = BoilerLine.processFrame(video_capture)
	elif(request == "RequestGear"):
		#Run a program specific to the gear
	else:
		response = 0

	sock.sendto(response, addr)		#Responds to the ip that sent the request

