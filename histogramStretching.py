import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('lenna.png',0)


min = img.min()
max = img.max()

result = np.zeros((img.shape[0],img.shape[1]), np.uint8)
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		result.itemset((i,j), ((img.item(i,j) - min)/(max - min))*255)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Original',(10,500), font, 1,(0,0,0),5)
cv2.putText(img,'Original',(10,500), font, 1,(255,255,255),2)
cv2.putText(result,'Resultado',(10,500), font, 1,(0,0,0),5)
cv2.putText(result,'Resultado',(10,500), font, 1,(255,255,255),2)

res = np.hstack((img,result))
cv2.imshow("Histogram Stretching",res)
cv2.waitKey(0)
cv2.destroyAllWindows()