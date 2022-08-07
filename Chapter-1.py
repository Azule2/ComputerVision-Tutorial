import cv2

#-----Chapter 1 -----(Read Image)
img = cv2.imread('test.png')

#Head Name Application and show img
cv2.imshow('Show Img', img)
cv2.waitKey(0)
#-----Chapter 1 -----(Video Camera)

#VideoCapture (0,1 Camera)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
 	success, img = cap.read()
 	cv2.imshow('Video', img)
  #press q (quit Application)
 	if cv2.waitKey(1) & 0xFF == ord('q'):
    
	 	break 
#-----Chapter 1 -----(Read Video)
cap = cv2.VideoCapture('test.mp4')
while True:
 	success, img = cap.read()
 	cv2.imshow('Video', img)
 	if cv2.waitKey(1) & 0xFF == ord('q'):
