import cv2

x = 0.5
y = 0.5

img = cv2.imread("lenna.png")

res = cv2.resize(img,None,fx=x, fy=y, interpolation = cv2.INTER_CUBIC)


cv2.imshow("Histogram",res)

cv2.waitKey(0)
cv2.destroyAllWindows()