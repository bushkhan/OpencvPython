import cv2

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
def empty(a):
    pass
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:
    img = cv2.imread("../Resources/car1.png")

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")

    print(h_min)
    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.waitKey(1)



