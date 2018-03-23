import cv2
import numpy as np

img = cv2.imread('lenna.png',0)

size = 3
kernel = np.array(
[[1,2,1],
[2,4,2],
[1,2,1]
])/16
mean = cv2.filter2D(img,-1,kernel)

result = np.multiply(img,2)-mean

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Original',(10,500), font, 1,(0,0,0),5)
cv2.putText(img,'Original',(10,500), font, 1,(255,255,255),2)
cv2.putText(result,'Resultado',(10,500), font, 1,(0,0,0),5)
cv2.putText(result,'Resultado',(10,500), font, 1,(255,255,255),2)

res = np.hstack((img,result))
cv2.imshow("Unsharp Mask",res)
cv2.waitKey(0)
cv2.destroyAllWindows()