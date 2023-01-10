import cv2
#
# img = cv2.imread("Resources/girl.png")
#
# cv2.imshow("Output",img)
#
# cv2.waitKey(0)


cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resized_Window", 700, 500)
cap = cv2.VideoCapture("Resources/vid.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Resized_Window", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
