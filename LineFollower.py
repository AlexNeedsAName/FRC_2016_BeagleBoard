import numpy as np
import cv2

def lineOffset(ret, frame):

    # Crop the image
    crop_img = frame#[60:120, 0:160]

    # Gaussian blur
    blur = cv2.GaussianBlur(crop_img,(5,5),0)

    #Convert to Hue, Saturation, and Value colorspace
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([0, 40, 0])
    upper_red = np.array([10, 255, 255])

    # Threshold the HSV image to get only red colors
    thresh = cv2.inRange(hsv, lower_red, upper_red)

    # Find the contours of the frame
    contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
	    cx = 0
            cy = 0

        cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)

        cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)

        if cx >= 80:
	    return cx-80

        if cx < 80:
            return -(80-cx)
    else:
        return 999
