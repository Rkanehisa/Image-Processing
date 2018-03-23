import cv2

img = cv2.imread("lenna.png")

x = 200
y = 150
angle = 45

rows = img.shape[0]
cols = img.shape[1]

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()