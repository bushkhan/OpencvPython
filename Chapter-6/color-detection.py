import cv2

img = cv2.imread("../Resources/car1.png")
cv2.namedWindow("Trackbars")
cv2.resize("Trackbars",640,240)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

img1 = cv2.resize(img,(400,300))
imgHSV1 = cv2.resize(imgHSV,(400,300))

cv2.imshow("Original",img1)

cv2.imshow("HSV",imgHSV1)

cv2.waitKey(0)