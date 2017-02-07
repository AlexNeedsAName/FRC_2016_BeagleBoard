import numpy as np
import cv2
import Tkinter
import tkMessageBox


top = Tkinter.Tk()


cap = cv2.VideoCapture(-1)
cap.set(3, 320)
cap.set(4, 240)


frame = 1


captureNum = 10


def captureCallBack():
    cv2.imwrite('image_' + str(captureNum) + '.png',frame)


B = Tkinter.Button(top, text="Capture", command=captureCallBack)
B.pack()


while 1:
    ret, frame = cap.read()
    cv2.circle(frame,(160,120),2,(255,0,0))
    # Display the frame
    cv2.imshow('frame', frame)
    top.update_idletasks()
    top.update()

    #quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
