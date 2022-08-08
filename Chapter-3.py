import cv2

#-----Chapter 3 -----(Resize Image)

img = cv2.imread('vehicle.jpg')
print(img.shape)
imgResize = cv2.resize(img,(200,300))
print(imgResize.shape)

cv2.imshow('Image',img)
cv2.imshow('Image Resize', imgResize)
cv2.waitKey(0)
#-----Chapter 3 -----(Cropped Image)
img = cv2.imread('vehicle.jpg')
print(img.shape)

imgCopped = img[0:200,200:500]

cv2.imshow('Image',img)
cv2.imshow('Cropped Image', imgCopped)

cv2.waitKey(0)
