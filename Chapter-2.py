import cv2
import numpy as np

#-----Chapter 2 ----- (ImgColor Gray)


img = cv2.imread('test.png')
#Img Color Gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray image', imgGray)
cv2.waitKey(0)

#-----Chapter 2 ----- (Blur Image)
import cv2

#-----Chapter 1 -----

#img = cv2.imread('girl.png')
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)

# while True:
# 	success, img = cap.read()
# 	cv2.imshow('Video', img)
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break 

# cv2.imshow('output', cap)
# cv2.waitKey(0)

#-----Chapter 2 -----(Blur Image)
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







