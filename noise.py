import numpy as np
import cv2

img = cv2.imread("noise.jpg")
averaging = cv2.blur(img, (5, 5))

cv2.imshow("Original image", img)
cv2.imshow("Averaging", averaging)
cv2.waitKey(0)
cv2.destroyAllWindows()

