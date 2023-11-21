import cv2
import numpy as np
kernal = np.ones((5,5),np.uint8)
print(kernal)
path =r"C:/Users/chait/Downloads/n2.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale",imgGray)
cv2.waitkey(0)
