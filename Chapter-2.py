import cv2
import numpy as np

#-----Chapter 2 ----- (ImgColor Gray)

img = cv2.imread('test.png')
#Img Color Gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray image', imgGray)
cv2.waitKey(0)

#-----Chapter 2 ----- (Blur Image)
img = cv2.imread('test.png')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)

cv2.imshow('BlurImage image', BimgBlur)
cv2.waitKey(0)
#-----Chapter 2 -----(Canny Image)
img = cv2.imread('test.png')

imgCanny = cv2.Canny(img, 150,200)

cv2.imshow('Canny image', imgCanny)
cv2.waitKey(0)







