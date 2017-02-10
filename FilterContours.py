import numpy as np
import cv2

def Filter(contours, minArea, maxArea, rectangularity, aspectRatio, aspectRatioTolerance):
    filteredContours = []
    for cnt in contours:
        if(IsTarget(cnt,minArea, maxArea, rectangularity, aspectRatio, aspectRatioTolerance)):
            filteredContours.append(cnt)
    return filteredContours

def IsTarget(contour,minArea, maxArea, rectangularity, aspectRatio, aspectRatioTolerance):
    area = cv2.contourArea(contour)
    _, _, w, h = cv2.boundingRect(contour)
    rectArea = w * h
    ar = w/h
    if abs(ar - aspectRatio) > aspectRatioTolerance:
        return False
    elif area < minArea or area < maxArea:
        return False
    elif (rectArea - area) * 100 / rectArea > rectangularity:  # check if the area is correct and the region is rectangular enough
        return False
    else:
        return True
