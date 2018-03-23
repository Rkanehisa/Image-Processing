import cv2
import numpy as np

img = cv2.imread("lenna.png",0)
thresh = 127
original_img = img.copy()
dithering = np.zeros((img.shape[0],img.shape[1]), np.uint8)


for y in range(img.shape[0]):
	for x in range(img.shape[1]):
		err = 0
		if(img[y][x] > 127):
			dithering[y][x] = 255
			err = img[y][x] - 255
		else:
			dithering[y][x] = 0
			err = img[y][x] - 0
		try:
			img[y][x+1] = img[y][x+1] + err*(7/16)
			img[y+1][x-1] = img[y+1][x-1] + err*(3/16)
			img[y+1][x] = img[y+1][x] + err*(5/16)
			img[y+1][x+1] = img[y+1][x+1] + err*(1/16)
		except:
			pass
		
res = np.hstack((original_img,dithering))
cv2.imshow("Dithering",res)
cv2.waitKey(0)
cv2.destroyAllWindows()