import cv2
import numpy as np

b = {255:True,0:False,True:255,False:0}

img1 = cv2.imread('img1.png',0)
img2 = cv2.imread('img2.png',0)


shape = img1.shape

img3 = np.zeros((shape[0],shape[1],3), np.uint8)

for i in range(shape[0]):
	for j in range(shape[1]):
		img3[i,j] = b[b[img1[i,j]] ^ b[img2[i,j]]]

cv2.imshow('image',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()