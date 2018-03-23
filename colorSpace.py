import cv2

img1 = cv2.imread("lenna.png")
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

cv2.imshow('image',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
