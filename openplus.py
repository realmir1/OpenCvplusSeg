#this project mini code for KoU AI team 

import cv2
import numpy as np

img = cv2.imread("example.jpg")  
img_resized = cv2.resize(img, (500, 500))
gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
contours, _ = cv2.findContours( opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = img_resized.copy()

cv2.drawContours(output, contours, -1, (0, 255, 0), 2)
cv2.imshow("Original", img_resized)
cv2.imshow("Gray", gray)
cv2.imshow("Threshold", thresh)
cv2.imshow("Segmented", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
