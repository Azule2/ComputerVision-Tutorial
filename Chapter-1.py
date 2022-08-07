import cv2

#-----Chapter 1 -----(Read Image)
img = cv2.imread('test.png')


cv2.imshow('Show Img', img)
cv2.waitKey(0)
