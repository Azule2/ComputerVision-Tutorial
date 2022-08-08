import cv2
import numpy as np
#-----Chapter-4----(Numpy Zeros and Create Line )

#create use numpy zeros size(512,512)
img = np.zeros((512,512,3),np.uint8)
#Create Line 
cv2.line(img, (0,0),(300,200),(255,30,30),3)

cv2.imshow("Image",img)

cv2.waitKey(0)
#-----Chapter-4----(Create rectangle )
img = np.zeros((512,512,3),np.uint8)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)#cv2.FILLED

cv2.imshow("Image",img)

cv2.waitKey(0)
#-----Chapter-4----(Create Circle And putText)
img = np.zeros((512,512,3),np.uint8)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img, 'SmartBite',(300,200), cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow("Image",img)

cv2.waitKey(0)
