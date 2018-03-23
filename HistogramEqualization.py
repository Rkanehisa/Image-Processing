import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lenna.png',0)
equ = cv2.equalizeHist(img)




font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Original',(10,500), font, 1,(0,0,0),5)
cv2.putText(img,'Original',(10,500), font, 1,(255,255,255),2)
cv2.putText(equ,'Equalizada',(10,500), font, 1,(0,0,0),5)
cv2.putText(equ,'Equalizada',(10,500), font, 1,(255,255,255),2)


res = np.hstack((img,equ))

cv2.imshow("Histogram",res)

cv2.waitKey(0)
cv2.destroyAllWindows()