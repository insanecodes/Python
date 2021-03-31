# import libraries
import cv2
import numpy as np

# load Image
img = cv2.imread("demo.jpg")

# Create Edge Mask
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur(gray, 5)
# detect and enhance edges
edges = cv2.adaptiveThreshold(
    gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# color quantization
# cartoonization
color = cv2.bilateralFilter(img, 8, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# show output image
cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
