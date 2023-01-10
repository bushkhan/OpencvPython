import cv2

img = cv2.imread("../Resources/girl.png")

cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Output", 700, 500)
cv2.imshow("Output",img)

cv2.waitKey(0)