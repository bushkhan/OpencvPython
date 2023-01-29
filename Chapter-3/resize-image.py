import cv2

img = cv2.imread("../Resources/girl.png")
cv2.imshow("Output",img)
print(img.shape)
imgResize = cv2.resize(img,(600,400))
#firstwidth then height
cv2.imshow("output",imgResize)
cv2.waitKey(0)