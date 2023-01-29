import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
img = cv2.imread("../Resources/girl.png")

cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gray Image", 500, 400)

cv2.namedWindow("Blur Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Blur Image", 500, 400)

cv2.namedWindow("Canny Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Canny Image", 500, 400)

cv2.namedWindow("Dilation Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Dilation Image", 500, 400)

cv2.namedWindow("Eroded Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Eroded Image", 500, 400)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)
