import cv2
import numpy as np
from statistics import median

def getMatrix(img,x,y,size):
	sum = []
	for i in range(x-size,x+size+1):
		for j in range(y-size,y+size+1):
			sum.append(img.item(i,j))
	return median(sum)

img = cv2.imread('lenna.png',0)


height = img.shape[0]
width = img.shape[1]

result = img.copy()
for i in range(1,height-1):
	for j in range(1,width-1):
		result.itemset((i,j),getMatrix(img,i,j,1))


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Original',(10,500), font, 1,(0,0,0),5)
cv2.putText(img,'Original',(10,500), font, 1,(255,255,255),2)
cv2.putText(result,'Resultado',(10,500), font, 1,(0,0,0),5)
cv2.putText(result,'Resultado',(10,500), font, 1,(255,255,255),2)

res = np.hstack((img,result))
cv2.imshow("Filtro Média",res)
cv2.waitKey(0)
cv2.destroyAllWindows()