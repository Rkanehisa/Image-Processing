import cv2 
import numpy as np

img = cv2.imread("lenna.png")

x = 200
y = 150

rows = img.shape[0]
cols = img.shape[1]

M = np.float32([[1,0,x],[0,1,y]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()