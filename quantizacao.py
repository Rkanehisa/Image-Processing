import cv2

img = cv2.imread('lenna.png',0)

shape = img.shape

for i in range(shape[0]):
	for j in range(shape[1]):
		if(img[i,j] < 64 and img[i,j] != 0):
			img[i,j] = 0
		elif(img[i,j] < 128):
			img[i,j] = (1*256/4)
		elif(img[i,j] < 192):
			img[i,j] = (2*256/4)
		elif(img[i,j] < 256):
			img[i,j] = (3*256/4)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
