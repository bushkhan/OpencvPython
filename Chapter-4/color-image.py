import cv2
import numpy as np

img =  np.zeros((512,512,3),np.uint8)
print(img.shape)
img[200:300,100:300] = 255,0,0 #blue color on image
cv2.imshow("Image",img)

cv2.waitKey(0)