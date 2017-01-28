import numpy as np
import cv2

lower = (40,96,118)
upper = (79,183,255)
minArea = 20
maxArea = 10000
rectangularity = 100
maxHeightDisparity = 30

def filterContours(contours, minArea, maxArea, rectangularity):
    filteredContours = []
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        area = cv2.contourArea(hull)
        _,_,w,h = cv2.boundingRect(hull)
        rectArea = w*h
        if area > minArea and area < maxArea and (rectArea - area) * 100 / rectArea < rectangularity:  #check if the area is correct and the region is rectangular enoug
            filteredContours.append(hull)
    return filteredContours

def findContourPosition(contour):#find the center of the rectangle
    x, y, w, h = cv2.boundingRect(contour)
    x += w / 2
    y += h / 2
    return x,y

def findSpring(ret, frame):
    frame = cv2.GaussianBlur(frame, (3, 3), 0)  # blur the frame to make less noise
    mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower, upper)
    _,contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Detect contours in the image
    contours = filterContours(contours, minArea, maxArea, rectangularity)
    if len(contours) == 2:
        x, y = findContourPosition(contours[0])  #find the positions of the contours
        z, w = findContourPosition(contours[1])
        if abs(y - w) < maxHeightDisparity:  #Check if the contours' heights are close
            x = (x + z) / 2
            y = (y + w) / 2  # find the center point between the contours
            return str(x),str(y)
    elif len(contours) > 2:
        for i in [0,len(contours) - 1]:#if there's more than 2 contours, find two at the same height.
            for j in [0,len(contours) - 1]:
                if i != j:
                    x, y = findContourPosition(contours[i])  # find the positions of the contours
                    z, w = findContourPosition(contours[j])
                    if abs(y - w) < maxHeightDisparity:
                        return str(x),str(y)
    return "0","0"
