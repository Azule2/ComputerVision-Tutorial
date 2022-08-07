import cv2
import numpy as np

#-----Chapter 2 -----


img = cv2.imread('test.png')
#Img Color Gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv.imshow('Gray image', imgGray)
cv2.waitKey(0)
