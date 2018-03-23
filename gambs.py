import cv2

img1 = cv2.imread("kongou.jpg",0)

for i in range(img1.shape[0]):
	for j in range(img1.shape[1]):
		if(int(img1[i][j]) > 127):
			img1[i][j] = 255
		else:
			img1[i][j] = 0

cv2.imwrite("img3.png",img1)