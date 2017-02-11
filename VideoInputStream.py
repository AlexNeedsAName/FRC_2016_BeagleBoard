#!/usr/bin/python

from threading import Thread
import numpy as np
import cv2
from subprocess import call

class VideoInputStream:
	def __init__(self, source=0):
		self.cap = cv2.VideoCapture(source)
		(self.grabbed, self.frame)=self.cap.read()
		self.stopped = False

	def start(self):
		inputThread = Thread(target=self.update, args=()).start()
		call(['./SetExposure.sh'], 10)
		return self

	def update(self):
		while True:
			if self.stopped:
				return
			(self.grabbed, self.frame) = self.cap.read()
			cv2.waitKey(1)

	def read(self):
		return self.grabbed, self.frame

	def stop(self):
		self.stopped = True
		
	def set(self, param, value):
		self.cap.set(param, value)
		
