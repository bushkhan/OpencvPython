import cv2

import numpy as np

img = cv2.imread('../Resources/girl.png')
imgResize = cv2.resize(img,(600,400))

imHor = np.hstack((imgResize,imgResize))

cv2.imshow("Horizontal", imHor)

cv2.waitKey(0)