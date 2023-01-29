import cv2

img = cv2.imread("../Resources/girl.png")

imgCropped = img[0:500,500:1000]
##first height then width
cv2.imshow("Output",imgCropped)

cv2.waitKey(0)