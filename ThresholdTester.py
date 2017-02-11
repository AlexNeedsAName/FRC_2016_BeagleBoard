import numpy as np
import cv2

cap = cv2.VideoCapture(-1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(15,1000)

def nothing(x):
    pass

cv2.namedWindow('image')#window for sliders

cv2.createTrackbar('min H','image',0,255,nothing)#create sliders for the threshold values
cv2.createTrackbar('max H','image',0,255,nothing)
cv2.createTrackbar('min S','image',0,255,nothing)
cv2.createTrackbar('max S','image',0,255,nothing)
cv2.createTrackbar('min V','image',0,255,nothing)
cv2.createTrackbar('max V','image',0,255,nothing)
cv2.createTrackbar('min area','image',0,50000,nothing)
cv2.createTrackbar('max area','image',0,50000,nothing)
cv2.createTrackbar('height difference', 'image', 0, 100,nothing)
cv2.createTrackbar('rectangularity', 'image', 0, 100,nothing)
cv2.createTrackbar('mode', 'image', 0,1,nothing)
cv2.createTrackbar('image', 'image', 0, 10, nothing)
while(1):
    #get the slider positions
    minH = cv2.getTrackbarPos('min H', 'image')
    minS = cv2.getTrackbarPos('min S', 'image')
    minV = cv2.getTrackbarPos('min V', 'image')
    maxH = cv2.getTrackbarPos('max H', 'image')
    maxS = cv2.getTrackbarPos('max S', 'image')
    maxV = cv2.getTrackbarPos('max V', 'image')
    minArea = cv2.getTrackbarPos('min area', 'image')
    maxArea = cv2.getTrackbarPos('max area', 'image')
    maxHeightDisparity = cv2.getTrackbarPos('height difference', 'image')
    mode = cv2.getTrackbarPos('mode', 'image')
    rectangularity = cv2.getTrackbarPos('rectangularity', 'image')
    imageNum = cv2.getTrackbarPos('image', 'image')
    if imageNum != 0:
        input = cv2.imread('image_'+str(imageNum)+'.png')
    else:
        ret, input = cap.read()
    frame = cv2.GaussianBlur(input, (5,5), 0) #blur the frame to make less noise
    # operations on the frame come here

    lower = (minH, minS, minV)
    upper = (maxH,maxS,maxV)

    mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV),lower,upper)  #create a mask that only covers pixels of the correct color

    #x,y = SpringDetect.findSpring(input, lower, upper, minArea, maxArea, rectangularity, maxHeightDisparity)
    #print str(x) + ', ' + str(y)
    #cv2.circle(frame, (x,y), 5, (0,255,0), 5)
    # Display the resulting frame
    if mode == 1:
        cv2.imshow('frame', input)
    else:
        cv2.imshow('frame', mask)
    #quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
