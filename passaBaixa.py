import cv2
import numpy as np

img = cv2.imread('lenna.png',0)


size = 3
kernel = np.array(
[[1,1,1],
[1,1,1],
[1,1,1]
])/9
result = cv2.filter2D(img,-1,kernel)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Original',(10,500), font, 1,(0,0,0),5)
cv2.putText(img,'Original',(10,500), font, 1,(255,255,255),2)
cv2.putText(result,'Resultado',(10,500), font, 1,(0,0,0),5)
cv2.putText(result,'Resultado',(10,500), font, 1,(255,255,255),2)

res = np.hstack((img,result))
cv2.imshow("Passa Baixa",res)
cv2.waitKey(0)
cv2.destroyAllWindows()