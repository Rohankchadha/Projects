import numpy as np
import cv2
# load image in color
img = cv2.imread("sample.jpg")
cv2.imshow("cat image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()